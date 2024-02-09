import connection

def llegir_taula():
    sql = '''SELECT * FROM POKEMON
    '''

    print(sql)

    connection.connection.execute(sql)
    dades = connection.connection.fetchall() #guardem en una tupla les dades obtingudes de la query

    for dada in dades : #les mostrem una a una en un print
        print (f'Pokemon: {dada} \n')

