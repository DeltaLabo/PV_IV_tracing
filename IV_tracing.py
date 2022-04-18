import controller_IV_reads
import pyvisa #protocolos comunicación.
import time 
from datetime import datetime
import os
import pandas as pd #analisis de datos
#from controller_IV_reads import Carga
#from controller_IV_reads import Fuente
##########################Buscar carga##################################


#Crear archivo csv
outputCSV = pd.DataFrame(columns = ["Timestamp", "Time", "Voltage", "Current"])
file_date = datetime.now().strftime("_%d_%m_%Y_%H_%M")
base = "/home/pi/tracing_data/"
os.makedirs(base,exist_ok = True)

rm = pyvisa.ResourceManager()
resources = rm.list_resources() # por defecto pasa '?*::INSTR'
print(resources)

for i in range(len(resources)):
    if resources[i].find("DL3A21") > 0:
        carga = rm.open_resource(resources[i]) 
        print("Carga DL3A21 encontrada")
        print(carga.query("*IDN?"))

Carga = controller_IV_reads.Carga(carga, "DL3021")


channel = 1
vset = 0
cset = 0
seconds = 0
past_time = datetime.now()
while vset < 23:
    Carga.set_mode("VOLT")
    Carga.remote_sense(False)
    Carga.fijar_voltaje(vset)
    Carga.encender_carga()
    time.sleep(1)
    # Medir carga y corriente.
    volt, current = Carga.medir_todo()
    print("Vset: ",vset)
    print("Lectura voltaje: ",volt)
    print("Lectura corriente: ",current)
    tiempo_actual = datetime.now()
    deltat = (tiempo_actual - past_time).total_seconds()
    seconds += deltat
    measuredf = pd.DataFrame({"Timestamp":tiempo_actual,"Time":round(seconds,2), "Voltage":volt, "Current":current},index=[0])
    outputCSV = pd.concat([outputCSV, measuredf], ignore_index=True)
    filename = base + "tracing_data" + file_date + ".csv"
    outputCSV.iloc[-1:].to_csv(filename, index=False, mode='a', header=False) #Create csv for tracing
    past_time = tiempo_actual
    vset += 0.5
