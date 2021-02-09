import pytz
from datetime import datetime, timedelta
from zones import zones

local_zone = 'America/Mexico_City'
zone_to_compare = 'Asia/Tokyo'

local_timezone = pytz.timezone(local_zone)
timezone_to_compare = pytz.timezone(zone_to_compare)

local_time = datetime.now().astimezone(local_timezone).strftime('%Y-%m-%d %H:%M:%S')
time_to_compare = datetime.now().astimezone(timezone_to_compare).strftime('%Y-%m-%d %H:%M:%S')

day = datetime.now().strftime('%Y-%m-%d')

def message(date, zone):
    print('\nFecha de referencia: {} hora de {}'.format(date, zone))
    print('Generando horarios de otros paises...\n')

def get_times(date):
    #Inicializamos el diccionario
    times = {"00pm": "X"}

    #Las zonas horarias son sacadas por ciudades
    for country in zones:
        dtc = date.astimezone(pytz.timezone(country[1]))
            #if country[1] == "Europe/Madrid":
            #    #Imprime la hora en formato de 24 hrs
            #    dtc = dtc.strftime("%-HH")
            #else:
            #    #Imprime la hora en formato de 12 hrs
            #   dtc = dtc.strftime("%-I%p")

        dtc = dtc.strftime("%-I:%M %p")

        try:
            times[dtc] = times[dtc] + country[0]
        except KeyError:
            times[dtc] = country[0]

        times[dtc] = times[dtc] + "]["

    for time, flag in times.items():
        if flag != "X":
            print(time.lower(), "[{}]".format(flag.strip("][")))


def time_difference(date1, date2):
    start_date = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
    end_date = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')
    diff = end_date - start_date
    #return diff.days*24 + diff.seconds/3600
    return int(diff.seconds/3600)


def update_time(old_time):
    updated_time = old_time - timedelta(hours=time_difference(local_time, time_to_compare))
    get_times(updated_time)

def insert_hour():
    hour = str(input('Ingrese la hora en el formato (hh) '))
    inserted_hour = day + ' ' + hour + ':00:00'
    inserted_hour = datetime.strptime(inserted_hour, '%Y-%m-%d %H:%M:%S')
    message(inserted_hour, zone_to_compare)
    update_time(inserted_hour)

def insert_hour_minutes():
    hour_minutes = str(input('Ingrese la hora en el formato (hh:mm) '))
    inserted_hour_minutes = day + ' ' + hour_minutes + ':00'
    inserted_hour_minutes = datetime.strptime(inserted_hour_minutes, '%Y-%m-%d %H:%M:%S')
    message(inserted_hour_minutes, zone_to_compare)
    update_time(inserted_hour_minutes)

def main():
    while True:
        command = str(input('''
            ¿Qué deseas convertir?
            [h]oras
            [m]inutos y horas
            [s]alir
        '''))

        if command.lower() == 'h':
            insert_hour()
        elif command.lower() == 'm':
            insert_hour_minutes()
        else:
            print('Bye Bye')
            break

if __name__ == '__main__':
    print('\n*=====Bienvenido al generador de horarios=====*')

    main()
