import csv
from sense_emu import SenseHat
import time

filename="datos_sensehat.csv" #Nombre del archivo csv
fieldnames=['Temperatura','Presión','Humedad'] #Nombre de los campos del archivo csv
sense=SenseHat() #Creamos el emulador

tiempo=10 #Muestras que vamos a tomar

with open(filename, 'w') as csvfile: #Abrimos el archivo como escritura y a continuación lo preparamos para escribir con formato csv
    writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(10): #Vamos escribiendo las muestras en el archivo a la vez que las tomamos
        temperatura=sense.temperature
        presion=sense.pressure
        humedad=sense.humidity

        writer.writerow({'Temperatura':str(temperatura),'Presión':str(presion),'Humedad':str(humedad)})
        time.sleep(1) #Pauso el programa un segundo entre muestra y muestra para tener tiempo de cambiar los valores en el emulador
