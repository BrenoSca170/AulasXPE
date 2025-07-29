import lxml.html as lx
import os
import pandas as pd
from encodings.aliases import aliases

# df = pd.read_csv('perfil_clientes.csv', sep=';')
# print(type(df))
#
# df.head()
# with open('perfil_clientes.txt', 'w') as f:
#     f.write(df.to_string())

Diretorio = './pesquisa'
lista_path = os.listdir(Diretorio)
lista_df = []
for arquivo in lista_path:
    local_arquivo = os.path.join(Diretorio, arquivo)
    df = pd.read_csv(local_arquivo, sep='|', encoding='latin1')
    lista_df.append(df)
df7 = pd.concat(lista_df)
with pd.ExcelWriter('lista_pesquisa.xlsx',) as f:
    df7.to_excel(f, index=False)

