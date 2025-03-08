from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtWidgets import QGridLayout, QWidget, QVBoxLayout, QLabel, QLineEdit, QDialog, QSpacerItem, QSizePolicy
from labjack import ljm
import pyqtgraph as pg

from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_config import Ui_Dialog
from ui.ui_app import Ui_Form
from views.stopwatch import Stopwatch


from controllers.workers import DataGenerator as DG


class ConfigDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupearUi()

    def setupearUi(self):
        self.setWindowTitle("Config Window")


# ventana importante

class AppWidget(QWidget, Ui_Form):
    # cambiar las etiquetas luego.
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # grafico
        self.barGraph = None

        # cronometro custom
        self.stopwatch = Stopwatch()
        self.timer_layout.addWidget(self.stopwatch)
        self.placeholder_widget.deleteLater()

        self.initUI()

    def initUI(self):
        # stopwatch
        self.timer_layout.setAlignment(Qt.AlignRight)

        # conectar botones

        # widget cronometro
        # botones: { start_btn, stop_btn, reset_btn }
        self.start_btn.clicked.connect(self.stopwatch.start)
        self.stop_btn.clicked.connect(self.stopwatch.stop)
        self.reset_btn.clicked.connect(self.stopwatch.reset)




class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        #labjack connection
        self.handle = None
        self.rango_ain = 10.0
        self.periodo_muestreo = 1

        # data generator
        self.thread_dg = None
        #self.worker = None

        #
        self.config_w = ConfigDialog() # config_window

        # is config okay

        """
        to do:
            - config Dialog, start in the first place
            - config is saved locally in a file
            - if config file is not found, show config window
            - you can edit config window locally with a button
            - after config, render de mainwindow or if config is changed, render a new mainwindow with the changes applied
        """

        self.is_config_okay = False
        print(self.is_config_okay)

        # mostrar ventnaa config
        self.show_new_window(True)



        # variables
        self.num_channels = 0
        self.num_in_channels = 0
        self.exp_name = ""
        self.colors = None
        self.channels = None
        self.temperatures = None
        self.ainput_list = None

        self.connection_status = False

        # diccionarios accesos para los elementos de los QGrid
        self.flux_in_spinboxes = None
        self.out_labels = None

        self.app_widget = AppWidget()


        self.initUI()



    def show_new_window(self, checked):
        self.config_w.buttonBox.button(QtWidgets.QDialogButtonBox.Apply).clicked.connect(self.set_config)
        self.config_w.show()


    def set_config(self):
        #self.is_config_okay = True

        self.display_app_layout()
        self.is_config_okay = True

        # disable input ch
        self.config_w.output_ch_input.setEnabled(False)
        self.config_w.close()




    def initUI(self):
        self.setWindowTitle("CCHEN APP")

        # configurar ui
        #self.display_channels(True)
        #print(self.flux_grid.rowCount(), self.flux_grid.columnCount())

        # style
        self.setStyleSheet("""
               
        """)

        self.app_widget.status_label.setText("Desconectado")

        # conectar botones
            # config window
        self.config_btn.clicked.connect(self.show_new_window)

            # connect buttn
        self.app_widget.connect_btn.clicked.connect(self.connect_labjack)


###################### BORRAR LUEGO YA QUE ESTO ESTA EN DATA READ, DEBES INTEGRARLO MEJOR ##################################3
    def connect_labjack(self):
        try:
            self.handle = ljm.openS("T7", "ANY", "ANY")
            # Configurar rangos para todos los canales
            for canal in self.ainput_list:
                ljm.eWriteName(self.handle, f"{canal}_RANGE", self.rango_ain)

            self.app_widget.status_label.setText("Conectado")
            self.connection_status = True

            print("Conexión exitosa con LabJack T7")
        except Exception as e:
            self.app_widget.status_label.setText("Error de conexion")
            self.connection_status = False
            print(f"Error de conexión: {str(e)}")


    def display_app_layout(self):
        exp_name = self.config_w.exp_line_edit.text()
        self.exp_name = exp_name
        # init app widget
        self.setWindowTitle(f"CCHEN APP - {self.exp_name}")

        # periodo de muestreo
        self.periodo_muestreo = self.config_w.periodo_muestreo_input.value()
        print(self.periodo_muestreo)

        if not self.is_config_okay:
            # renderizar inputs y outputs para cada canal
            self.display_channels()

            # iniciar configuracion de los canales
            self.init_channels()

            # iniciar grafico esta vez con datos estaticos
            self.setup_graph()


            self.setup_thread()
            self.setup_connections()


        self.app_layout.addWidget(self.app_widget)


    def display_channels(self): # afecta al app widget
        """
        Demasiado complejo y poco practico. Make it simple. Haz una ventana previa con las configuraciones basicas y tras eso renderizas el numero de canales directamente
        No deberias hacer esto.
        """
        self.num_channels = self.config_w.output_ch_input.value()


        # Crear nuevos layouts
        flux_grid = QGridLayout()
        temp_q_grid = QGridLayout()

        flux_grid.setSpacing(10)
        temp_q_grid.setSpacing(10)

        # diccionarios para acceso a los elementos:
        self.flux_in_spinboxes = {} # almacena QDoubleSpinBox, llaves son "CHn"
        self.out_labels = {} # almacena QLabel, llaves son tuplas ( "q" | "temp", n_channel )


        # Primeros elementos estáticos en flux_grid
        flux_grid.addWidget(QtWidgets.QLabel("Flujo:"), 1, 0)

        # Primeros elementos estáticos en temp_q_grid
        temp_q_grid.addWidget(QtWidgets.QLabel("Temperatura:"), 1, 0)
        temp_q_grid.addWidget(QtWidgets.QLabel("Q:"), 2, 0)

        # Agregar la primera columna fija
        flux_grid.addWidget(QtWidgets.QLabel(f"CH 1\n(input)"), 0, 1)

        spin_box_1 = QtWidgets.QDoubleSpinBox()

        flux_grid.addWidget(spin_box_1, 1, 1)

        temp_q_grid.addWidget(QtWidgets.QLabel(f"CH 1\n(input)"), 0, 1)

        label_1_temp = QtWidgets.QLabel("empty")
        label_1_q = QtWidgets.QLabel("empty")

        temp_q_grid.addWidget(label_1_temp, 1, 1)
        temp_q_grid.addWidget(label_1_q, 2, 1)


        # almacenar referencias
        self.flux_in_spinboxes[1] = spin_box_1
        self.out_labels[("temp", 1)] = label_1_temp
        self. out_labels[("q", 1)] = label_1_q

        # Agregar columnas dinámicas según el número de canales
        for i in range(self.num_channels):
            col = i + 2  # Comienza desde la segunda columna dinámica

            # Input en flux_grid
            flux_grid.addWidget(QtWidgets.QLabel(f"CH {col}"), 0, col)

            spin_box_i = QtWidgets.QDoubleSpinBox()

            flux_grid.addWidget(spin_box_i, 1, col)

            # Output en temp_q_grid
            temp_q_grid.addWidget(QtWidgets.QLabel(f"CH {col}"), 0, col)

            label_i_temp = QtWidgets.QLabel("empty")
            label_i_q = QtWidgets.QLabel("empty")

            temp_q_grid.addWidget(label_i_temp, 1, col)
            temp_q_grid.addWidget(label_i_q, 2, col)

            # almacenar referencias
            self.flux_in_spinboxes[col] = spin_box_i
            self.out_labels[("temp", col)] = label_i_temp
            self.out_labels[("q", col)] = label_i_q

        # Reasignar layouts nuevos al contenedor
        self.app_widget.flux_layout.addLayout(flux_grid)

        # add horizontal spacer to look good
        self.app_widget.ch_grid_layout.addLayout(temp_q_grid)
        #self.app_widget.ch_grid_layout.addItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))


    def init_channels(self):

        channels = []
        colors = []
        temperatures = []
        ainput_list = []

        t_dummy = 22.0

        for i in range(self.num_channels + 1):
            channels.append(f"CH {i+1}")
            ainput_list.append(f"AIN{i}")

            if i == 0: # primer canal
                colors.append("#3584E4") # canal in agua
                temperatures.append( t_dummy)

            else:
                colors.append("#DB5C5C") # canales out agua
                temperatures.append(t_dummy + 0.5 * i)

        self.channels = channels
        self.colors = colors
        self.temperatures = temperatures
        self.ainput_list = ainput_list
        print(ainput_list)


    def setup_graph(self):
        """Configura el gráfico principal"""
        self.app_widget.out_graph.setTitle("Temperatura por Canal")
        self.app_widget.out_graph.setLabel("left", "Temperatura (°C)")
        self.app_widget.out_graph.setLabel("bottom", "Canales")
        self.app_widget.out_graph.setXRange(0, len(self.channels) - 1)
        self.app_widget.out_graph.setMouseEnabled(x = False, y = True)

        print(self.channels)
        print(self.temperatures)

        # Configurar barras
        self.app_widget.barGraph = pg.BarGraphItem(
            x=range(len(self.channels)),
            height = self.temperatures,
            width = 0.5,
            brush = 'r' # actualizar a self.colors
        )

        self.app_widget.out_graph.addItem(self.app_widget.barGraph)

        self.app_widget.out_graph.getAxis('bottom').setTicks([[(i, ch) for i, ch in enumerate(self.channels)]])


############################################################################ cambios a adaptar ##################################################
### AUN NO EStan conectados con lA interfaz actual ##############################################################################################


    def setup_thread(self):
        """Configurar el sistema de hilos para la generación de datos"""
        self.thread_dg = QThread()
        self.worker = DG(RANGO_AIN = self.rango_ain, interval =  self.periodo_muestreo, CANALES =  self.ainput_list)
        self.worker.moveToThread(self.thread_dg)

        # Conectar señales
        # self.thread_dg.started.connect(self.worker.generate_data)

        ## Fake data
        self.thread_dg.started.connect(self.worker.generate_data_dummy)

        self.worker.data_ready.connect(self.update_temperatures)
        self.worker.finished.connect(self.thread_dg.quit)

        # Iniciar hilo
        self.thread_dg.start()

    def setup_connections(self):
        """Conectar señales y slots"""

        # estos botones tambien registran el experimento
        self.app_widget.start_btn.clicked.connect(self.start_experiment)

        # quitar logica de pausa a logica de detener
        self.app_widget.stop_btn.clicked.connect(self.toggle_pause)

        self.app_widget.reset_btn.clicked.connect(self.reset_experiment)

        self.import_btn.clicked.connect(self.import_experiment)

        # save
        self.app_widget.save_btn.clicked.connect(self.save_experiment)

    def start_experiment(self):
        """Iniciar experimento"""
        self.worker.set_paused(False)
        #self.start_btn.setEnabled(False)
        #self.pause_btn.setEnabled(True)

    def toggle_pause(self):
        """Pausar/Reanudar captura"""
        paused = not self.worker._is_paused
        self.worker.set_paused(paused)
        #self.pause_btn.setText("Reanudar" if paused else "Pausar")

    def update_temperatures(self, new_data):
        """Actualizar temperaturas con nuevos datos"""
        self.temperatures = new_data
        self.app_widget.barGraph.setOpts(height=self.temperatures)

        # Actualizar labels ESTO NO ESTA IMPLEMENTADO

        #######################################################################################################################
        for i in range(self.num_channels + 1):
            #getattr(self, f"out_t{i + 1}").setText(f"T{i + 1}: {self.temperatures[i]:.1f}°C")
            self.out_labels[("temp", i + 1)].setText(f"{self.temperatures[i]:.1f} °C")
            self.out_labels[("q", i + 1)].setText("not implemented")

        self.calculate_outputs()

    def calculate_outputs(self):
        """Calcular resultados basados en inputs"""
        try:
            # Corregir en base a los diccionarios implementados

            input_voltage = self.app_widget.v_in.value()
            input_current = self.app_widget.current_in.value()

            power = input_voltage * input_current

            flows = [float(  self.flux_in_spinboxes[i+1].value()) for i in range(self.num_channels + 1) ]

            weighted_avg = sum(t * w for t, w in zip(self.temperatures, flows)) / power

            # note implemented
            self.app_widget.p_out.setText(f"{power:.2f} W")
            self.app_widget.q_tot_out.setText(f"{13:.2f}")
            self.app_widget.eff_out.setText(f"{weighted_avg:.2f}")

        except Exception as e:
            print(f"Error en cálculos: {e}")
            self.app_widget.p_out.setText("Error en inputs")
            self.app_widget.q_tot_out.setText("Verifica valores")
            self.app_widget.eff_out.setText("")

    def closeEvent(self, event):
        """Manejar cierre de la aplicación"""
        self.worker.stop()
        self.thread_dg.quit()
        self.thread_dg.wait()
        super().closeEvent(event)

    # Métodos para implementar (puedes agregar tu lógica aquí)
    def save_experiment(self):
        """Guardar experimento (por implementar)"""
        print("Guardar experimento - Implementar lógica")

    def reset_experiment(self):
        """Resetear experimento, debe reiniciar el archivo de data registrada (por implementar)"""
        print("Resetear - Implementar lógica")

    def import_experiment(self):
        """Importar experimento (por implementar)"""
        print("Importar experimento - Implementar lógica")