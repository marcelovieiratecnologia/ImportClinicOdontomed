from ImportClinicOdontomed.config import connect
from ImportClinicOdontomed.lendoCSV import lerArq

# Variaveis Globais
listLinhas = []

def profExisteNoPostGreSql(nome_profissional):
    # conectar = connect()
    # cursor = conectar.cursor()
    cursor = connect().cursor()
    sqlSelect = "SELECT * FROM tb_om_profissionais WHERE nome_profissional LIKE "+"'%"+ nome_profissional +"%'"
    cursor.execute(sqlSelect)
    row = cursor.rowcount
    cursor.close()
    connect().close()
    # for c in cursor:
    #     print(c)
    if row > 0:
        return True
    else:
        return False

def maxIdProf():
    cursor = connect().cursor()
    sql = "SELECT MAX(id) FROM tb_om_profissionais"
    cursor.execute(sql)
    idmax = cursor.fetchone()[0] + 1
    return idmax
# print(maxIdProf())

def importProfPostGreSql():
    listLinhas = lerArq()
    nome_profissional = listLinhas[0][1]
    # print(str.upper(nome_profissional))
    # print(nome_profissional)
    if profExisteNoPostGreSql(nome_profissional) == False:
        # print(listLinhas[0][1])
        conecta = connect()
        cursor = conecta.cursor()
        sqlInsert = "INSERT INTO tb_om_profissionais (id,nome_profissional,cidades_id,orgao_emissor_id) VALUES("
        sqlInsert += str(maxIdProf()) +","
        sqlInsert += "'"+ str.upper(nome_profissional) +"',"
        sqlInsert += str(99) +","
        sqlInsert += str(99)+")"
        print(sqlInsert)
        cursor.execute(sqlInsert)
        conecta.commit()
        cursor.close()

# importProfPostGreSql()





