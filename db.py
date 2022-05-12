from os import getenv
import psycopg2

POSTGRES_HOST = getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PASSWORD = getenv('POSTGRES_PASSWORD', 'password')
POSTGRES_USER = getenv('POSTGRES_USER', 'user')
POSTGRES_DB = getenv('POSTGRES_DB', 'db')

def init_db():
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD)
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS observations;')
    cur.execute('CREATE TABLE observations (id serial PRIMARY KEY,'
                                    'text varchar (150) NOT NULL,'
                                    'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                    )
    conn.commit()
    cur.close()
    conn.close()

def insert(text: str):
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD)
    cur = conn.cursor()
    cur.execute(f"INSERT INTO observations (text) VALUES ('{text}')")
    
    conn.commit()
    cur.close()
    conn.close()

def list():
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM observations;")
    result = cur.fetchone()
    print(result, flush=True)
    conn.commit()
    cur.close()
    conn.close()
    return result
