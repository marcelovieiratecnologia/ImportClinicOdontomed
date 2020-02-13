
# import pandas as pd
# print(pd.read_csv('clinica.csv', encoding='latin-1'))

# import csv
# with open('clinica.csv', 'rb') as arq:
#     for linha in arq.readline():
#         print(linha)
#     # print(arq.readline())
#
#     # linhas = csv.reader(arq, delimiter=':', quoting=csv.QUOTE_NONE)
#     # for linha in linhas:
#     #     print(linha)


arquivo = open('clinica.csv', 'r', encoding='latin-1')
linhas = arquivo.readlines()
countLinha = 0
for linha in linhas:
    countLinha = countLinha + 1
    print(linha)

print('Total de linhas é: ', countLinha)