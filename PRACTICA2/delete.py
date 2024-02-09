import connection

def eliminar_pokemon():

    sql = '''DELETE FROM POKEMON WHERE pokemon_id = 1
    '''

    print (sql)

    connection.connection.execute(sql) #Executem la query
    connection.conn.commit() #Guardem els canvis