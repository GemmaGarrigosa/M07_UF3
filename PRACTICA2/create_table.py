import psycopg2

from connection import *
resposta = input('Vols connectar amb la base de dades? (si/no)')

if resposta == 'si':
    try:
            conn = psycopg2.connect(
                database="practica2",
                user="gemma",
                password="system",
                host="localhost",
                port="5432"
            )

            connection = conn.cursor()
            #Creem la taula de pokemons a la BD


            sql = '''CREATE TABLE POKEMON(
                            pokemon_id SERIAL PRIMARY KEY,
                            pokemon_name VARCHAR(255) NOT NULL,
                            pokemon_type1 VARCHAR(255) NOT NULL,
                            pokemon_type2 VARCHAR(255),
                            pokemon_weight FLOAT NOT NULL,
                            pokemon_height FLOAT NOT NULL               
            )'''

            print(sql)

            #Enviar query
            connection.execute(sql)

            #Commit per a fer els canvis
            conn.commit()

    except (Exception,psycopg2.Error) as error:
        print("Error", error)
    finally:
        conn.close()

else:
    print('No has volgut crear la taula')