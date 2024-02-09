import connection

def actualitza_pokemon():
    sql = '''UPDATE POKEMON SET pokemon_name = 'Pepe' WHERE pokemon_id = 1
    '''

    print(sql)

    connection.connection.execute(sql) #Executem la query
    connection.conn.commit() #Guardem els canvis