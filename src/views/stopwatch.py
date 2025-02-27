import sys
from datetime import time

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()

        self.time = QTime(0, 0, 0, 0) # horas, minutos, segundos
        self.time_label = QLabel("00:00:00", self)

        self.timer = QTimer(self)

        self.initUI()


    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        # Estilo
        self.setStyleSheet("""
            QLabel {
                font-size: 25px;
                background-color: #1E1F22;
                border-radius: 5px;
                color: #308AD2;
                padding: 10px;
                max-width: 150px;
                max-height: 50px;
            }
        """)

        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self): # pause
        self.timer.stop()

    def reset(self):
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText("00:00:00")

    def format_time(self, time):
        # time to str
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10 # 2 cifras en lugar de 3

        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:02d}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

        print(self.time)
