import os
import psycopg2


def init_db():
    conn = psycopg2.connect(
        host="localhost",
        database="db",
        user='user',
        password='password')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS observations;')
    cur.execute('CREATE TABLE observations (id serial PRIMARY KEY,'
                                    'text varchar (150) NOT NULL,'
                                    'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                    )
    conn.commit()
    cur.close()
    conn.close()
