import psycopg2
from ImportClinicOdontomed.config import connectPostGreSql

def insertPostgres_tb_om_entrada_saida():
    conectar = connectPostGreSql()
    cur = conectar.cursor()
    # sqlInsert = 'Insert into tb_om_cidades (id, nome_cidade, uf) values (%s,%s,%s);'
    # value = (99, 'CIDADE', 'GG')
    sqlInsert = "INSERT INTO tb_om_entrada_saida () values()"
    # sqlSelect = "Select * from tb_om_entrada_saida"
    cur.execute(sqlInsert)

    for c in cur:
        print(c)

    conectar.commit()