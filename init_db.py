import psycopg2

# esta archivo se encarga de conectarse a la base de datos y  ejecutar sentencias sql 
# aqui repasar el database 
conn = psycopg2.connect(database = "Locales", host= "localhost", user = "postgres", password = "12345", port= "5433")
cur = conn.cursor()

# aquia se insertan valores en una tabla ya creada
#cur.execute('''INSERT INTO locals (name, city, address) VALUES ('Cafe de los Angelitos', 'Caceres', 'Av. Rivadavia 2100')''')

conn.commit()

cur.close()
conn.close()