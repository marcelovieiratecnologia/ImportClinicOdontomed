import csv
from datetime import datetime
#
# usando pandas, porém tenho que instalar a biblioteca
# import pandas as pd
# print(pd.read_csv('clinica.csv', 'rb', encoding='latin-1'))

# arquivo = open('clinica.csv', 'r', encoding='latin-1')
# def lerArq(arquivo):
#     linhas = arquivo.readlines()
#     countLinha = 0
#     for linha in linhas:
#         countLinha = countLinha + 1
#         print(linha)
#     # print('Total de linhas é: ', countLinha)
#     return linhas
# lerArq(arquivo)

# usando o csv

listarquivo = [] # guardando os dados certos em uma lista para serem importados
arquivo = '2019JaneiroPlanilhaCaixaOdontoMed.csv'

def lerArq():
    with open(arquivo, encoding='latin-1') as csvfile:
        readCSV = csv.reader(csvfile,delimiter=';')
        # print(readCSV)
        for line in readCSV:
            dictrow = {}
            # print(line)
            dictrow['data'] = datetime.strptime(line[0], '%d/%m/%Y').date()
            dictrow['profissional'] = line[1]
            dictrow['paciente'] = line[2]
            dictrow['conv_part'] = line[3]
            dictrow['deb_cred'] = line[4]
            dictrow['tp_credito'] = line[5]
            dictrow['parcelas'] = line[6]
            dictrow['porcentagem'] = line[7]
            dictrow['entrada'] = line[8]
            dictrow['saida'] = line[9]
            dictrow['saldo'] = line[10]
            dictrow['desconto'] = line[11]
            dictrow['total_liquido'] = line[12]
            dictrow['campo_controle'] = line[13]
            listarquivo.append(dictrow)
        # row.pop() # usando o pop() sem passar argumento nenhum removo o ultimo item da minha lista que no caso desse .CSV é a linha TOTAL e não preciso dela.
    return listarquivo

# arquivo = lerArq()
# for linha in arquivo:
#     print(linha)

# # Essa é a primeira linha que tenho que começar
# print(lerArq()[0]) # ['01/07/2019', 'Tatiana', 'Tereza Leite de Prado', 'PARTICULAR', 'DINHEIRO', '', '', '0,00%', 'R$ 250,00', 'R$ 0,00', 'R$ 250,00', 'R$ 0,00', 'R$ 250,00']
# # Penultima linha , até onde tenho que ir
# print(lerArq()[-2]) # ['01/07/2019', 'Tatiana', 'Tereza Leite de Prado', 'PARTICULAR', 'DINHEIRO', '', '', '0,00%', 'R$ 250,00', 'R$ 0,00', 'R$ 250,00', 'R$ 0,00', 'R$ 250,00']#
# # Ultima linha que tenho que desconsiderar
# print(lerArq()[-1]) # ['R$ 12.534,93', 'R$ 1.679,74', 'R$ 10.855,19', 'R$ 97,80', 'R$ 10.75']

# l = lerArq(arquivo)
# print(l[0][0])
# lerArq(arq201907)

