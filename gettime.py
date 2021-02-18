import pytz
from zones import zones
from datetime import datetime, timedelta
from settings import local_zone, zone_to_compare

local_timezone = pytz.timezone(local_zone)
timezone_to_compare = pytz.timezone(zone_to_compare)

local_time = datetime.now().astimezone(local_timezone).strftime('%Y-%m-%d %H:%M:%S')
time_to_compare = datetime.now().astimezone(timezone_to_compare).strftime('%Y-%m-%d %H:%M:%S')

def get_times(date):
    #Inicializamos el diccionario
    times = {"00pm": "X"}

    #Las zonas horarias son sacadas por ciudades
    for country in zones:
        dtc = date.astimezone(pytz.timezone(country[1]))

        dtc = dtc.strftime("%A %-I:%M %p")

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
