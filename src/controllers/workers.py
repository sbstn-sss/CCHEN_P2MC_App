from PyQt5.QtCore import QObject, QThread, pyqtSignal
import random
import numpy as np

from labjack import ljm
import time
import sys
from datetime import datetime
from models.data_read import LabJackDataRead as LJDR

class DataGenerator(QObject):
    data_ready = pyqtSignal(list)
    finished = pyqtSignal()

    def __init__(self, RANGO_AIN = 1.0, interval=0.5, CANALES = ["AIN0", "AIN1", "AIN2", "AIN3", "AIN4", "AIN5", "AIN6"]):
        super().__init__()
        self.interval = interval
        self.CANALES = CANALES

        self._is_running = True
        self._is_paused = False

        self.monitor = LJDR(RANGO_AIN=RANGO_AIN, CANALES=CANALES)


    def generate_data(self):
        while self._is_running:
            if not self._is_paused:
                mediciones = self.monitor.update_data()
                if mediciones:
                    data = [(10000 * (1.0580 +mediciones[channel]['y'] ) if mediciones[channel]['y']  < 0 else mediciones[channel]['y'] - 1.0102717876434326       )  for channel in self.monitor.CANALES]
                    self.data_ready.emit(data)
                    #print(data)
            QThread.msleep(int(self.interval * 1000))


    def generate_data_dummy(self):
        while self._is_running:
            if not self._is_paused:
                #mediciones = self.monitor.update_data()
                #if mediciones:
                data = [ np.random.random() * 10 + 20  for channel in self.CANALES]
                self.data_ready.emit(data)
            QThread.msleep(int(self.interval * 1000))


    def stop(self):
        self._is_running = False
        self.monitor.shutdown()
        self.finished.emit()

    def set_paused(self, paused):
        self._is_paused = paused
