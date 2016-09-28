import psycopg2

from psycopg2.extras import DictCursor


def get_connection():

    conn = None

    try:
        conn = psycopg2.connect(
            dbname="sparks_flask",
            host="localhost",
            user="postgres",
            password="123456"
        )
        print "PostgreSQL: Conectado com sucesso!"
    except:
        print "PostgreSQL: Erro ao criar conexao!"

    return conn


def get_cursor(conn):
    return conn.cursor(cursor_factory=DictCursor)
