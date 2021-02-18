from modulos.inserts import insert_hour, insert_hour_minutes

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
