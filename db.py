import psycopg2
from psycopg2 import pool

#crear un pool de conexiones
connection_pool = pool = pool.SimpleConnectionPool(
    1,20,
        database="biblioteca3a",
        user="postgres",
        password="bran19",
        host="localhost",
        port="5432"
    )

def conetar():
        return connection_pool.getconn()

def desconectar(conn):
            connection_pool.putconn(conn)