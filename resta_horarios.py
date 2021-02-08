import pytz
import datetime
from datetime import datetime

hour = ""
date_to_convert = ""
day = datetime.now().strftime("%Y-%m-%d")

print("Bienvenido al generador de horarios\n")
confirmation = str(input("Quiere que su conversion incluya minutos? Teclee Y: "))

if confirmation.lower() == 'y': 
    hour = str(input("Ingrese su hora local (hh:mm): "))
    date_to_convert = day + " " + hour + ":00"
else:
    hour = str(input("Ingrese su hora local (hh): "))
    date_to_convert = day + " " + hour + ":00:00"

date_to_convert = datetime.strptime(date_to_convert, "%Y-%m-%d %H:%M:%S")

print()
print(date_to_convert)
print("Generando horarios...\n")

zones = [
    ["JP", "Asia/Tokyo"],
    ["MX", "America/Mexico_City"],
    ["CO", "America/Bogota"],
    ["CL", "America/Santiago"],
    ["AR", "America/Buenos_Aires"],
    ["PE", "America/Lima"],
    ["ES", "Europe/Madrid"]
]

#Inicializamos el diccionario
times = {"00pm": "X"}

#Las zonas horarias son sacadas por ciudades

for country in zones:
    dtc = date_to_convert.astimezone(pytz.timezone(country[1]))
    #if country[1] == "Europe/Madrid":
    #    #Imprime la hora en formato de 24 hrs
    #    dtc = dtc.strftime("%-HH")
    #else:
    #    #Imprime la hora en formato de 12 hrs
    #   dtc = dtc.strftime("%-I%p")
    
    #dtc = dtc.strftime("%-I%p")
    #dtc = dtc.strftime("%-I:%-mm %p")
    #dtc = dtc.strftime("%H:%M %p")
    dtc = dtc.strftime("%-I:%M %p")

    try:
        times[dtc] = times[dtc] + country[0]
    except KeyError:
        times[dtc] = country[0]

    times[dtc] = times[dtc] + " "

for time, flag in times.items():
    if flag != "X":
        print(time.lower(), flag.strip())
