from datetime import datetime, timedelta
from message import message
from gettime import update_time

date = datetime.now().strftime('%Y-%m-%d')
year = datetime.now().strftime('%Y-')

def insert_day():
    inserted_day = str(input('Ingrese el mes y dia o deje en blanco para usar el dia actual: '))
    if len(inserted_day) != 0:
        return year + inserted_day
    else:
        return date

def insert_hour():
    hour = str(input('Ingrese la hora en el formato (hh) '))
    inserted_hour = insert_day() + ' ' + hour + ':00:00'
    inserted_hour = datetime.strptime(inserted_hour, '%Y-%m-%d %H:%M:%S')
    message(inserted_hour)
    update_time(inserted_hour)

def insert_hour_minutes():
    hour_minutes = str(input('Ingrese la hora en el formato (hh:mm) '))
    inserted_hour_minutes = insert_day() + ' ' + hour_minutes + ':00'
    inserted_hour_minutes = datetime.strptime(inserted_hour_minutes, '%Y-%m-%d %H:%M:%S')
    message(inserted_hour_minutes, zone_to_compare)
    update_time(inserted_hour_minutes)
