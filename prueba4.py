import pytz
from datetime import datetime

def restar_fechas(fecha1, fecha2):
    start_date = datetime.strptime(fecha1, '%Y-%m-%d %H:%M:%S')
    end_date = datetime.strptime(fecha2, '%Y-%m-%d %H:%M:%S')
    diff = end_date - start_date
    print("Diff ", diff)
    print("Diff days", diff.days)
    print("Diff seconds", diff.seconds)
    #return diff.days*24 + diff.seconds/3600
    return diff.seconds/3600

timezone = pytz.timezone("America/Mexico_city")
timezone2 = pytz.timezone("Asia/Tokyo")

local = datetime.now().astimezone(timezone).strftime('%Y-%m-%d %H:%M:%S')

tokyo = datetime.now().astimezone(timezone2).strftime('%Y-%m-%d %H:%M:%S')

print(restar_fechas(local, tokyo))
