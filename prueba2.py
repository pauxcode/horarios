import datetime
from datetime import datetime

hour = ""
date_to_convert = ""
day = datetime.now().strftime("%Y-%m-%d")

confirmation = str(input("Deseas convertir minutos y segundos? Teclee Y/N: "))

if confirmation.lower() == 'y': 
    hour = str(input("Ingrese la hora de referencia (hh:mm:ss): "))
    date_to_convert = day + " " + hour
else:
    hour = str(input("Ingrese la hora de referencia (hh): "))
    date_to_convert = day + " " + hour + ":00:00" 

date_to_convert = datetime.strptime(date_to_convert, "%Y-%m-%d %H:%M:%S")

print()
print(date_to_convert)
