import pandas as pd
import numpy as np
import os

dirdadosvendas = './dados_vendas_produtos.csv'
dirvendasprodutos = './vendas_produtos_financeiros.csv'

if not os.path.exists(dirdadosvendas) or not os.path.exists(dirvendasprodutos):
    print('Arquivo CSV não encontrado!')
    exit()

dados = pd.read_csv(dirdadosvendas, sep=';', encoding='Latin1')
vendas = pd.read_csv(dirvendasprodutos, sep=';')

excel_file = 'output.xlsx'
with pd.ExcelWriter(excel_file) as f:
    dados.to_excel(f, index=False, sheet_name='Dados')
    vendas.to_excel(f, index=False, sheet_name='Vendas')

dfdados = dados[['Nome do vendedor','Produto vendido','Quantidade unitária','Valor do produto','Valor da venda','Data da compra','Localização']]
dfvendas = vendas[['Produto','Quantidade','Preco_Unitario','Valor_Total','Data','Estado']]

# if dfdados.isna().any().any():
#     print('dados has Na')
#     print(dfdados.isna().sum()[dfdados.isna().sum() > 0])

# if dfvendas.isna().any().any():
#     print('vendas has Na\n')
#     print(dfvendas.isna().sum()[dfvendas.isna().sum() > 0])
# if dfdados.isna().any().any():
#     print('dados has Na\n')
#     print(dfdados.isna().sum()[dfdados.isna().sum() > 0])
# else:
#     print('no Na')

vendasduplicatas = dfvendas.duplicated()

print(vendasduplicatas.sum())
dadosduplicatas = dfdados.duplicated()
print(dadosduplicatas.sum())
# Corrige a vírgula decimal se necessário e converte pra float
dfvendas['Valor_Total'] = dfvendas['Valor_Total'].astype(str).str.replace(',', '.').astype(float)

# Filtra só as vendas do estado de SP
vendas_sp = dfvendas[dfvendas['Estado'] == 'SP']

# Calcula a média
media_sp = vendas_sp['Valor_Total'].mean()

print(f'Média do valor total das vendas para SP: R$ {media_sp:.2f}')

estado = input('Digite o estado desejado: ').strip().upper()
dfdados['Localização'] = dfdados['Localização'].str.strip().str.upper()
df_estado = dfdados[dfdados['Localização'] == estado].copy()

# Garante que a coluna 'Quantidade unitária' tá em formato numérico
df_estado['Quantidade unitária'] = pd.to_numeric(df_estado['Quantidade unitária'], errors='coerce')

# Calcula o desvio padrão (padrão populacional: ddof=0, padrão amostral: ddof=1)
desvio_padrao = df_estado['Quantidade unitária'].std()

print(f'Desvio padrão da quantidade unitária para PE: {desvio_padrao:.2f}')
