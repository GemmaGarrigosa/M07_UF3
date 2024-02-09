import connection

def actualitza_pokemon():
    sql = '''UPDATE POKEMON SET pokemon_name = 'Pepe' WHERE pokemon_id = 1
    '''

    print(sql)

    connection.connection.execute(sql)
    connection.conn.commit()