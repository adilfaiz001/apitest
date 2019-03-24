'''
script for creating table with given schema.
'''

import psycopg2

conn = psycopg2.connect(database = "apitest", user = "postgres", password = "98939605", host = "127.0.0.1", port = "5432")
print "Opened database successfully"

cur = conn.cursor()

cur.execute('''CREATE TABLE TB_LOC
            (key                 TEXT   PRIMARY KEY    NOT NULL,
            place_name           TEXT,
            admin_name1          TEXT,
            latitude             DECIMAL,
            longitude            DECIMAL,
            accuracy             DECIMAL);''')

print "Table created successfully"

conn.commit()
conn.close()