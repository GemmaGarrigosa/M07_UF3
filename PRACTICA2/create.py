import connection

def crear_pokemon():

    sql = '''INSERT INTO POKEMON (pokemon_name,pokemon_type1,pokemon_type2,pokemon_weight,pokemon_height) VALUES ('Bulbasaur','Grass','Venom',15.2,2.04)
    '''

    print(sql)

    # Enviar query
    connection.connection.execute(sql)
    # Commit per a confirmar la transacció
    connection.conn.commit()