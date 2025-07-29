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
for arquivo in lista_path:
    print(arquivo)
    encodings = ['utf-8', 'latin1', 'iso-8859-1', 'cp1252']
    for encoding in encodings:
        try:
            with open(f'{Diretorio}/{arquivo}', 'r', encoding=encoding) as f:
                html = lx.fromstring(f.read())
                content = html.text_content()
                print(content)
                break
        except UnicodeDecodeError:
            continue
