import connection

#Creem la taula de pokemons a la BD
# id, nom , tipus1, tipus2, pes, mida

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