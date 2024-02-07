import psycopg2


conn = psycopg2.connect(
    database = "practica2",
    user = "gemma",
    password ="system",
    host = "localhost",
    port ="5432"
)

connection = conn.cursor() #comprova la connexió amb PostgreSQL

print(connection)