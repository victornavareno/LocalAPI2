import psycopg2

from models.Local import Local

# establecemos la conexion
def db_connection():
    conn = psycopg2.connect(database = "Locales", host= "localhost", user = "postgres", password = "12345", port= "5433")

def get_all_locals():
    conn = db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM locals")
    rows = cur.fetchall()
    locals = []
    for row in rows:
        local = Local(row[1], row[2], row[3])
        locals.append(local)
    cur.close()
    conn.close()
    return locals

def get_local_by_id(local_id):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM locals WHERE id = %s", (local_id))
    row = cur.fetchone()
    local = Local(row[1], row[2], row[3])
    cur.close()
    conn.close()
    if local:
        return local
    else:
        print ("Local not found")
        None

def create_local(local):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO locals (name, city, address) VALUES (%s, %s, %s)", (local.name, local.city, local.address))
    new_local_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return new_local_id

def update_local(local_id, local):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE locals SET name = %s, city = %s, address = %s WHERE id = %s", (local.name, local.city, local.address, local_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_local(local_id):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM locals WHERE id = %s", (local_id))
    conn.commit()
    cur.close()
    conn.close()