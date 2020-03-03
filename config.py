#!/usr/bin/python
from configparser import ConfigParser
import psycopg2

def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # Ler os parametros de conexão
        params = config()
        # conecta no PostGreSQL Server
        # print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        # Cria um cursor
        # cur = conn.cursor() Irei criar o cursor apenas na minha função
        # @@@@@@ Não estou usando essas instruções abaixo @@@@@@@@
        # # Executa uma Declaração
        # print('PostgreSQL database version:')
        # cur.execute('SELECT version()')
        # # display the PostgreSQL database server version
        # db_version = cur.fetchone()
        # print(db_version)
        # # close the communication with the PostgreSQL
        # cur.close()
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
    #         print('Conexão Finalizada/Fechada.')
    return conn