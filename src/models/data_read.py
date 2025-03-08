from labjack import ljm
import time
import sys
from datetime import datetime

class LabJackDataRead():
    def __init__(self, RANGO_AIN=1.0, CANALES=["AIN0", "AIN1", "AIN2", "AIN3", "AIN4", "AIN5", "AIN6"]):
        self.handle = None
        self.RANGO_AIN = RANGO_AIN
        self.N_CANALES = len(CANALES)
        self.CANALES = CANALES or [f'AIN{i}' for i in range(N_CANALES)]

        self.data = {canal: {'x': 0, 'y': 0} for canal in self.CANALES}
        self.start_time = time.time()
        self.connect_labjack()

    def connect_labjack(self):
        try:
            self.handle = ljm.openS("T7", "USB", "ANY")
            for canal in self.CANALES:
                ljm.eWriteName(self.handle, f"{canal}_RANGE", self.RANGO_AIN)
            print("✅ Conexión exitosa con LabJack T7")

        except Exception as e:
            print(f"❌ Error de conexión: {str(e)}")
            #sys.exit(1)

    def update_data(self):
        try:
            valores = ljm.eReadNames(self.handle, len(self.CANALES), self.CANALES)

            t = time.time() - self.start_time
            for i, canal in enumerate(self.CANALES):
                #valor = ljm.eReadName(self.handle, canal)
                self.data[canal] = {'x': t, 'y': valores[i]}
                valor_rango = ljm.eReadName(self.handle, f"{canal}_RANGE")

                if i == 0:
                    print("AIN0", t,  valores[i])
                    #print(f"Rango aplicado en {canal}: {valor_rango}")
            return self.data
        except Exception as e:
            print(f"❌ Error de lectura: {str(e)}")
            return None

    def shutdown(self):
        if self.handle:
            ljm.close(self.handle)
            print("🔌 LabJack desconectado")
