#!/usr/bin/python
import psycopg2
import csv
from config import config
from lendoCSV import lerArq

# arquivo = 'clinica.csv'
# linhas = lerArq(arquivo)
# print(linhas[:][:]) # Todas as Linhas e Colunas do arquivo

# Variáveis Globais
linhas = []


''' Layout do Arquivo:
 ===== ============== ========== ===================== ========== ============ ============ === ========= ======= ======= ========== ===============  
|  1  |       2      |    3     |          4          |   5      |      6     |      7     | 8 |    9    |   10  |  11   |    12    |      13       |
 ===== ============== ========== ===================== ========== ============ ============ === ========= ======= ======= ========== ===============
|DATA | PROFISSIONAL | PACIENTE | CONVENIO/PARTICULAR |  D/C     | TP CRÉDITO | N PARCELAS | % | ENTRADA | SAIDA | SALDO | DESCONTO | TOTAL LIQUIDO |
 ===== ============== ========== ===================== ========== ============ ============ === ========= ======= ================== =============== 
                                    particular          débito      a vista
                                    odontoprev          crédito     a prazo
                                    bradesco
                                    interodonto
====================================================================================================================================================                                    
'''

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

def testeConectaPostGres_ExecutaSql():
    # print(connect())
    conectar = connect()
    cur = conectar.cursor()
    sql = "Select * from tb_om_entrada_saida;"
    cur.execute(sql)
    resultado = cur.fetchall()
    print(resultado)

def insertPostgres_tb_om_entrada_saida():
    conectar = connect()
    cursor = conectar.cursor()
    # sqlInsert = 'Insert into tb_om_cidades (id, nome_cidade, uf) values (%s,%s,%s);'
    # value = (99, 'CIDADE', 'GG')
    sqlInsert = "INSERT INTO tb_om_entrada_saida () values()"
    cursor.execute(sqlInsert, value)
    conectar.commit()


# def sql():
#     #conn = None
#     # Ler os parametros de conexão
#     params = config()
#     # conecta no PostGreSQL Server
#     conn = psycopg2.connect(**params)
#     # Cria um cursor
#     cursor = conn.cursor()
#     # Uma declaração
#     SqlStm = 'SELECT * FROM tb_om_entrada_saida;'
#     cursor.execute(SqlStm)
#     # rows = cursor.fetchone()
#     rows = cursor.fetchall()
#     # print(rows[:])
#     for row in rows:
#         print(row[:])



if __name__ == '__main__':
    # testeConectaPostGres_ExecutaSql()

    arquivo = 'clinica.csv'
    # linhas var global
    linhas = lerArq(arquivo)
    # print(linhas[0][0])
    # print(linhas[0])
    # sql()
    # connect()
    #insert()
    insertPostgres_tb_om_entrada_saida()



