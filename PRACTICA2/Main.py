import create_table
import connection
import psycopg2

#Programa empieza, connecta bbdd, pregunta si quieres crear la tabla, switch de metodes
try:
    response = input('Vols crear la taula? (si/no)')

    if response == 'si':
        create_table.crear_taula()

    action = input(',Llegir(R)'
                   ',Actualitzar(U)'
                   ',Eliminar(D)').upper()


    if action == 'R':
        print('metode read')
    elif action == 'U':
        print('metode update')
    elif action == 'D':
        print('metode delete')
    else:
        print('Susplau introdueix una acció vàlida')


except (Exception, psycopg2.Error) as error:
    print("Error", error)
finally:
    connection.conn.close()
