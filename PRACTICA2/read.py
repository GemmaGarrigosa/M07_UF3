import connection

def llegir_taula():
    sql = '''SELECT * FROM POKEMON
    '''

    print(sql)

    connection.connection.execute(sql)
    dades = connection.connection.fetchall()

    for dada in dades :
        print (f'Pokemon: {dada} \n')

    connection.conn.commit()