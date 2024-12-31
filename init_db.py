import psycopg2

# Connect to the database
try:
    conn = psycopg2.connect(
        database="Locales",
        host="localhost",
        user="postgres",
        password="12345",
        port="5433"
    )
    cur = conn.cursor()
    
    # Execute a query to fetch all rows
    cur.execute("SELECT * FROM locals;")
    rows = cur.fetchall()
    
    # Print the rows
    for row in rows:
        print(row)
    
    # Close the cursor and connection
    cur.close()
    conn.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)
