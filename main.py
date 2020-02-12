#!/usr/bin/python
import psycopg2
import csv
from config import config



def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # Ler os parametros de conexão
        params = config()

        # conecta no PostGreSQL Server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # Cria um cursor
        cur = conn.cursor()

        # Executa uma Declaração
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Conexão Finalizada/Fechada.')


def sql():
    #conn = None
    # Ler os parametros de conexão
    params = config()
    # conecta no PostGreSQL Server
    conn = psycopg2.connect(**params)
    # Cria um cursor
    cursor = conn.cursor()
    # Uma declaração
    SqlStm = 'SELECT * FROM tb_om_cidades;'
    cursor.execute(SqlStm)
    # bases = cursor.fetchone()
    bases = cursor.fetchall()

    print(bases[:])

if __name__ == '__main__':
    sql()
    # connect()
