import psycopg2

conn = psycopg2.connect(database = "apitest", user = "postgres", password = "98939605", host = "127.0.0.1", port = "5432")
print "Opened database successfully"

cur = conn.cursor()

cur.execute('''CREATE TABLE tb_in
            (key                 TEXT   PRIMARY KEY    NOT NULL,
            place_name           TEXT,
            admin_name1          TEXT,
            latitude             TEXT,
            longitude            TEXT,
            accuracy             TEXT);''')

print "Table created successfully"

conn.commit()
conn.close()