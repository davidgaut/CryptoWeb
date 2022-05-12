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
                                    'currency varchar (150) NOT NULL, value REAL,'
                                    'date_prediction date DEFAULT CURRENT_TIMESTAMP);'
                                    )
    conn.commit()
    cur.close()
    conn.close()

def insert(currency: str, prediction: float):
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD)
    cur = conn.cursor()
    cur.execute(f"INSERT INTO observations (currency, value) VALUES ('{currency}',{prediction})")
    
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
    # result = cur.fetchone()
    result = cur.fetchall()
    print(result, flush=True)
    conn.commit()
    cur.close()
    conn.close()
    return result
