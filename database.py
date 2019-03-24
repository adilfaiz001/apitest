import psycopg2
from config import config
 
def insert_data(pin, place_name, admin_name1, latitude, longitude):

    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        

        # create a cursor
        cur = conn.cursor()
        
        # execute a statement
        cur.execute("INSERT INTO tb_in (key, place_name, admin_name1, latitude, longitude) \
                        VALUES (%s, %s, %s, %s, %s);",(pin, place_name, admin_name1, latitude, longitude));

        conn.commit()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
