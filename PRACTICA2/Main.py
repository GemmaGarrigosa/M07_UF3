import create_table
import connection
import psycopg2
import create
import read
import update
import delete
#Programa empieza, connecta bbdd, pregunta si quieres crear la tabla, switch de metodes
try:
    response = input('Vols crear la taula? (si/no)')

    if response == 'si':
        create_table.crear_taula()

    while True:
        action = input('Crear(C)'
                       ',Llegir(R)'
                       ',Actualitzar(U)'
                       ',Eliminar(D),'
                       'Sortir(0)').upper()


        if action =='R':
            read.llegir_taula()

        elif action == 'U':
            update.actualitza_pokemon()

        elif action == 'D':
            delete.eliminar_pokemon()

        elif action == 'C':
            create.crear_pokemon()

        elif action == '0':
            print('bye :D ')
            break


except (Exception, psycopg2.Error) as error:
    print("Error", error)
finally:
    connection.conn.close()
