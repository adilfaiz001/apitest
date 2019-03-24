import psycopg2
from config import config
 
def insert_data(key, place_name, admin_name1, latitude, longitude):

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
        
        # check pincode existance
        cur.execute("SELECT key FROM tb_loc WHERE key = %s",(key,))
        flag = cur.fetchone() is not None           # checking for same pincode

        if flag:
            return False

        else:
            #check for nearby latitude and lonitude, (I took +5 and -5 range)
            lower_lat = latitude - 5
            upper_lat = latitude + 5
            lower_longitude = longitude - 5
            upper_longitude = longitude + 5

            cur.execute("SELECT key FROM tb_loc \
                        WHERE (latitude BETWEEN %s AND %s) \
                        AND   (longitude BETWEEN %s AND %s);",(lower_lat,upper_lat,lower_longitude,upper_longitude));
            bol_near = cur.fetchone() is not None
            
            if bol_near:
                return False
            else:
                #adding unique pincode and not nearby latitud+longitude to database.
                cur.execute("INSERT INTO tb_loc (key, place_name, admin_name1, latitude, longitude) \
                                VALUES (%s, %s, %s, %s, %s);",(key, place_name, admin_name1, latitude, longitude));
                conn.commit()
                conn.close()
                return True

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
