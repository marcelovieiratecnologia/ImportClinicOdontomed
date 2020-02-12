
import pandas as pd
print(pd.read_csv('clinica.csv', encoding='latin-1'))

# import csv
#
# with open('../ArquivosClinica/2019 AGOSTO - Planilha Caixa OdontoMed.csv', 'rb') as arq:
#     linhas = csv.reader(arq, delimiter=':', quoting=csv.QUOTE_NONE)
#     for linha in linhas:
#         print(linha)
#
