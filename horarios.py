import pytz
from datetime import datetime

zones = [
    ["JP", "Asia/Tokyo"],
    ["MX", "America/Mexico_City"],
    ["CO", "America/Bogota"],
    ["CL", "America/Santiago"],
    ["AR", "America/Buenos_Aires"],
    ["PE", "America/Lima"],
    ["ES", "Europe/Madrid"]
]

timezone1 = pytz.timezone("America/Mexico_City")
timezone2 = pytz.timezone("Asia/Tokyo")

day = datetime.now().strftime("%Y-%m-%d")
local = datetime.now().astimezone(timezone1).strftime("%Y-%m-%d %H:%M:%S")
tokyo = datetime.now().astimezone(timezone2).strftime("%Y-%m-%d %H:%M:%S")

def time_difference(date1, date2):
    start_date = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
    end_date = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')
    diff = end_date - start_date
    print("Diff ", diff)
    print("Diff days", diff.days)
    print("Diff seconds", diff.seconds)
    #return diff.days*24 + diff.seconds/3600
    return int(diff.seconds/3600)

def insert_hour(hour):
    date_to_convert = day + " " + hour + ":00:00"
    return date_to_convert

def insert_hour_minutes(hour_minutes):
    date_to_convert = day + " " + hour_minutes + ":00"
    return date_to_convert

def get_time(date):
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

def main():
    var_time_difference = time_difference(local, tokyo)

    while True:
        command = str(input('''
            ¿Qué deseas convertir?
            [h]oras
            [m]inutos y horas
            [s]alir
        '''))

        if command.lower() == 'h':
            hour = int(input("Ingrese su hora local (hh): "))
            corr_hour = hour - var_time_difference
            date_to_convert = insert_hour(str(corr_hour))
        elif command.lower() == 'm':
            hour_minutes = str(input("Ingrese su hora local (hh:mm): "))
            date_to_convert = insert_hour_minutes(hour_minutes)
        else:
            break

        date_to_convert = datetime.strptime(date_to_convert, "%Y-%m-%d %H:%M:%S")

        #time_difference(date_to_convert, )

        print("\nSu hora local elejida es: ", date_to_convert)
        print("Generando horarios de otros paises...\n")

        get_time(date_to_convert)

if __name__ == '__main__':
    print("*=====Bienvenido al generador de horarios=====*")

    main()
