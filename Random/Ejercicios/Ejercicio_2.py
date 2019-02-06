import datetime
import time
import os

for i in range(60):
    os.system('cls')  # Limpiar pantalla windows
    fecha_actual = datetime.datetime.now()
    print("{}:{}:{}".format(fecha_actual.hour,fecha_actual.minute,fecha_actual.second))
    time.sleep(1)
