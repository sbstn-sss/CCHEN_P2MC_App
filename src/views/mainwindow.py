from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QWidget, QVBoxLayout, QLabel, QLineEdit, QDialog

from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_config import Ui_Dialog
from ui.ui_app import Ui_Form
from views.stopwatch import Stopwatch

# otra ventana

# class AnotherWindow(QWidget):
#     """
#
#     This "window" is a QWidget. If it has no parent, it
#     will appear as a free-floating window as we want.
#
#     """
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel("Another Window")
#         self.text = QLineEdit("This is another window")
#
#         self.button = QtWidgets.QPushButton("Continue")
#
#         layout.addWidget(self.label)
#         layout.addWidget(self.text)
#         layout.addWidget(self.button)
#
#         self.setLayout(layout)
#
#         #connections
#
#         self.button.clicked.connect(self.toggle_window)
#
#
#     def toggle_window(self, checked):
#         if self.isVisible():
#             self.hide()


class ConfigDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupearUi()

    def setupearUi(self):
        self.setWindowTitle("Config Window")

class AppWidget(QWidget, Ui_Form):
    # cambiar las etiquetas luego.
    def __init__(self):
        super().__init__()
        self.setupUi(self)



        # cronometro custom
        self.stopwatch_2 = Stopwatch()
        self.timer_layout_2.addWidget(self.stopwatch_2)
        self.placeholder_widget_2.deleteLater()

        self.initUI()

    def initUI(self):
        # stopwatch
        self.timer_layout_2.setAlignment(Qt.AlignRight)

        # conectar botones

        # widget cronometro
        # botones: { start_btn, stop_btn, reset_btn }
        self.start_btn_2.clicked.connect(self.stopwatch_2.start)
        self.stop_btn_2.clicked.connect(self.stopwatch_2.stop)
        self.reset_btn_2.clicked.connect(self.stopwatch_2.reset)




class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

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

        # # cronometro custom
        # self.stopwatch = Stopwatch()
        # self.timer_layout.addWidget(self.stopwatch)
        # self.placeholder_widget.deleteLater()
        #

        self.app_widget = AppWidget()


        self.initUI()



    def show_new_window(self, checked):
        self.config_w.buttonBox.button(QtWidgets.QDialogButtonBox.Apply).clicked.connect(self.setConfig)
        self.config_w.show()


    def setConfig(self):
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

        # cambio de numero de canales
        #self.output_ch_input.valueChanged.connect(self.display_channels)

       #  # stopwatch
       #  self.timer_layout.setAlignment(Qt.AlignRight)
       #
       #  # conectar botones
       #
       #      # config window
        self.config_btn.clicked.connect(self.show_new_window)
       #
       #
       #
       #
       #      # widget cronometro
       #  #botones: { start_btn, stop_btn, reset_btn }
       #  self.start_btn.clicked.connect(self.stopwatch.start)
       #  self.stop_btn.clicked.connect(self.stopwatch.stop)
       #  self.reset_btn.clicked.connect(self.stopwatch.reset)


    def display_app_layout(self):
        exp_name = self.config_w.exp_line_edit.text()
        self.exp_name = exp_name
        # init app widget
        self.setWindowTitle(f"CCHEN APP - {self.exp_name}")

        if not self.is_config_okay:
            self.display_channels()

        self.app_layout.addWidget(self.app_widget)


    def display_channels(self): # afecta al app widget
        """
        Demasiado complejo y poco practico. Make it simple. Haz una ventana previa con las configuraciones basicas y tras eso renderizas el numero de canales directamente
        No deberias hacer esto.
        """
        self.num_channels = self.config_w.output_ch_input.value()
        print(self.num_channels)

        # Crear nuevos layouts
        flux_grid = QGridLayout()
        temp_q_grid = QGridLayout()

        flux_grid.setSpacing(10)
        temp_q_grid.setSpacing(10)

        # Primeros elementos estáticos en flux_grid
        flux_grid.addWidget(QtWidgets.QLabel("Flujo:"), 1, 0)

        # Primeros elementos estáticos en temp_q_grid
        temp_q_grid.addWidget(QtWidgets.QLabel("Temperatura:"), 1, 0)
        temp_q_grid.addWidget(QtWidgets.QLabel("Q:"), 2, 0)

        # Agregar la primera columna fija
        flux_grid.addWidget(QtWidgets.QLabel(f"CH 1\n(input)"), 0, 1)
        flux_grid.addWidget(QtWidgets.QDoubleSpinBox(), 1, 1)

        temp_q_grid.addWidget(QtWidgets.QLabel(f"CH 1\n(input)"), 0, 1)
        temp_q_grid.addWidget(QtWidgets.QLabel("empty"), 1, 1)
        temp_q_grid.addWidget(QtWidgets.QLabel("empty"), 2, 1)

        # Agregar columnas dinámicas según el número de canales
        for i in range(self.num_channels):
            col = i + 2  # Comienza desde la segunda columna dinámica

            # Input en flux_grid
            flux_grid.addWidget(QtWidgets.QLabel(f"CH {col}"), 0, col)
            flux_grid.addWidget(QtWidgets.QDoubleSpinBox(), 1, col)

            # Output en temp_q_grid
            temp_q_grid.addWidget(QtWidgets.QLabel(f"CH {col}"), 0, col)
            temp_q_grid.addWidget(QtWidgets.QLabel("empty"), 1, col)
            temp_q_grid.addWidget(QtWidgets.QLabel("empty"), 2, col)

        # Reasignar layouts nuevos al contenedor
        self.app_widget.flux_layout_2.addLayout(flux_grid)
        self.app_widget.ch_grid_layout_2.addLayout(temp_q_grid)


