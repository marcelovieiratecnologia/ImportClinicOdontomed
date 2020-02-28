import csv

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
row = []
# arquivo = 'clinica.csv'
def lerArq(arquivo):
    with open(arquivo, encoding='latin-1') as csvfile:
        readCSV = csv.reader(csvfile,delimiter=';')
        # print(readCSV)
        for rows in readCSV:
            # print(row)
            row.append(rows)
    return row

# l = lerArq(arquivo)
# print(l[0][0])
