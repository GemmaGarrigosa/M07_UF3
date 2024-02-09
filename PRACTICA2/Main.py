import connection
import psycopg2

#IMPORTS DE TAULES
import create_table
import create
import read
import update
import delete

#Prova a connectar-se només al main
try:
    response = input('Vols crear la taula? (si/no)')

    if response == 'si':
        create_table.crear_taula()

    while True: #Bucle que anirà preguntant al usuari quina acció vol fer
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
            break #S'acaba el bucle


except (Exception, psycopg2.Error) as error:
    print("Error", error) #Si falla la connexió que surti un error
finally:
    connection.conn.close() #Tanquem sempre la connexió
