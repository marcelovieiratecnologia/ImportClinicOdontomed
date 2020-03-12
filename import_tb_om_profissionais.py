from ImportClinicOdontomed.config import connectPostGreSql
from ImportClinicOdontomed.lendoCSV import lerArq

# Variaveis Globais
conGlobal = connectPostGreSql()
curGlobal = conGlobal.cursor()

# listLinhas = []
listLinhas = lerArq()


def profExisteNoPostGreSql(nome_profissional):
    # print(nome_profissional)
    nome_profissional = str.upper(nome_profissional)
    conectar = connectPostGreSql()
    cursor = conectar.cursor()
    sqlSelect = "SELECT * FROM tb_om_profissionais WHERE nome_profissional LIKE "+"'%"+ nome_profissional.strip() +"%'"
    cursor.execute(sqlSelect)
    row = cursor.rowcount
    cursor.close()
    conectar.close()
    # for c in cursor:
    #     print(c)
    if row == 0:
        return False

def maxIdProf():
    conectar = connectPostGreSql()
    cursor = conectar.cursor()
    sql = "SELECT MAX(id) FROM tb_om_profissionais"
    cursor.execute(sql)
    idmax = cursor.fetchone()[0] + 1
    return idmax
# print(maxIdProf())

def import_prof_postGreSql():
    # listLinhas = lerArq()
    # nome_profissional = listLinhas[0][1]
    # print(str.upper(nome_profissional))
    # print(nome_profissional)
    qtde_profissionais_inseridos = 0
    for l in listLinhas:
        # print(l['campo_controle'])
        if l['campo_controle'] == '2': # essa Key defini como a linha tem um profissional
            if profExisteNoPostGreSql(l['profissional']) == False:
                qtde_profissionais_inseridos += 1
                # print(listLinhas[0][1])
                sqlInsert = "INSERT INTO tb_om_profissionais (id,nome_profissional,cidades_id,orgao_emissor_id) VALUES("
                sqlInsert += str(maxIdProf()) +","
                # sqlInsert += "'"+ str.upper(nome_profissional) +"',"
                sqlInsert += "'" + str.upper(l['profissional']) + "',"
                sqlInsert += str(99) +","
                sqlInsert += str(99)+")"
                print(sqlInsert)
                curGlobal.execute(sqlInsert)
                conGlobal.commit()
    print('Quantidade de PROFISSIONAIS Inseridos na base foi de: ', qtde_profissionais_inseridos)

def executa_import_profissionais():
    import_prof_postGreSql()
    curGlobal.close()
    conGlobal.close()

# executa_import_profissionais()


