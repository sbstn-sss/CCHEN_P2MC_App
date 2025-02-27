from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from ui.ui_mainwindow import Ui_MainWindow

from views.stopwatch import Stopwatch

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # cronometro custom
        self.stopwatch = Stopwatch()
        self.timer_layout.addWidget(self.stopwatch)
        self.placeholder_widget.deleteLater()

        self.initUI()


    def initUI(self):
        self.setWindowTitle("CCHEN APP")

        # configurar ui


        # style
        self.setStyleSheet("""
               
        """)



        # stopwatch
        self.timer_layout.setAlignment(Qt.AlignRight)

        # conectar botones con el widget cronometro

        #botones: { start_btn, stop_btn, reset_btn }
        self.start_btn.clicked.connect(self.stopwatch.start)
        self.stop_btn.clicked.connect(self.stopwatch.stop)
        self.reset_btn.clicked.connect(self.stopwatch.reset)


