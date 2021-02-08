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

day = datetime.now().strftime("%Y-%m-%d")

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
    while True:
        command = str(input('''
            ¿Qué deseas convertir?
            [h]oras
            [m]inutos y horas
            [s]alir
        '''))

        if command.lower() == 'h':
            hour = str(input("Ingrese su hora local (hh): "))
            date_to_convert = insert_hour(hour)
        elif command.lower() == 'm':
            hour_minutes = str(input("Ingrese su hora local (hh:mm): "))
            date_to_convert = insert_hour_minutes(hour_minutes)
        else:
            break

        date_to_convert = datetime.strptime(date_to_convert, "%Y-%m-%d %H:%M:%S")

        print("\nSu hora local elejida es: ", date_to_convert)
        print("Generando horarios de otros paises...\n")

        get_time(date_to_convert)

if __name__ == '__main__':
    print("*=====Bienvenido al generador de horarios=====*")

    main()
