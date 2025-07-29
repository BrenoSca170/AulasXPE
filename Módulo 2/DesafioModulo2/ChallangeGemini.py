import pandas as pd
import numpy as np
import os

# Define os caminhos para os arquivos CSV
dirdadosvendas = './dados_vendas_produtos.csv'
dirvendasprodutos = './vendas_produtos_financeiros.csv'

# Verifica se os arquivos CSV existem
if not os.path.exists(dirdadosvendas) or not os.path.exists(dirvendasprodutos):
    print('Arquivo CSV não encontrado!')
    exit()

# Carrega os dados dos arquivos CSV
dados = pd.read_csv(dirdadosvendas, sep=';', encoding='Latin1')
vendas = pd.read_csv(dirvendasprodutos, sep=';')

# Cria um arquivo Excel com os dados carregados (opcional, mantido do script original)
excel_file = 'output.xlsx'
with pd.ExcelWriter(excel_file) as f:
    dados.to_excel(f, index=False, sheet_name='Dados')
    vendas.to_excel(f, index=False, sheet_name='Vendas')

# Seleciona as colunas relevantes dos DataFrames
dfdados = dados[['Nome do vendedor','Produto vendido','Quantidade unitária','Valor do produto','Valor da venda','Data da compra','Localização']]
dfvendas = vendas[['Produto','Quantidade','Preco_Unitario','Valor_Total','Data','Estado']]

# Verifica e imprime a soma de duplicatas (mantido do script original)
vendasduplicatas = dfvendas.duplicated()
print(f'Número de linhas duplicadas em dfvendas: {vendasduplicatas.sum()}')
dadosduplicatas = dfdados.duplicated()
print(f'Número de linhas duplicadas em dfdados: {dadosduplicatas.sum()}')

# Corrige a vírgula decimal na coluna 'Valor_Total' e converte para float
dfvendas['Valor_Total'] = dfvendas['Valor_Total'].astype(str).str.replace(',', '.').astype(float)

# Filtra vendas do estado de SP e calcula a média (mantido do script original)
vendas_sp = dfvendas[dfvendas['Estado'] == 'SP']
media_sp = vendas_sp['Valor_Total'].mean()
print(f'Média do valor total das vendas para SP: R$ {media_sp:.2f}')

# Solicita o estado ao usuário e calcula o desvio padrão (mantido do script original)
# Nota: Esta parte interage com o usuário. Se estiver executando em um ambiente não interativo,
# você pode comentar ou remover esta seção.
# estado = input('Digite o estado desejado: ').strip().upper()
# dfdados['Localização'] = dfdados['Localização'].str.strip().str.upper()
# df_estado = dfdados[dfdados['Localização'] == estado].copy()
# df_estado['Quantidade unitária'] = pd.to_numeric(df_estado['Quantidade unitária'], errors='coerce')
# desvio_padrao = df_estado['Quantidade unitária'].std()
# print(f'Desvio padrão da quantidade unitária para {estado}: {desvio_padrao:.2f}')

# --- Início da lógica para responder à pergunta ---

# Garante que a coluna 'Quantidade' está em formato numérico, tratando possíveis erros
dfvendas['Quantidade'] = pd.to_numeric(dfvendas['Quantidade'], errors='coerce')

# Remove linhas onde 'Quantidade' não pôde ser convertida para número (NaN)
dfvendas_cleaned = dfvendas.dropna(subset=['Quantidade'])

# Calcula a soma da coluna "Quantidade" para cada "Produto"
soma_quantidade_por_produto = dfvendas_cleaned.groupby('Produto')['Quantidade'].sum()

# Encontra o produto com o maior total de unidades vendidas
produto_mais_vendido = soma_quantidade_por_produto.idxmax()
maior_quantidade_vendida = soma_quantidade_por_produto.max()

print("\n--- Análise de Quantidade de Produtos Vendidos ---")
print("Soma da quantidade por produto:")
print(soma_quantidade_por_produto)
print(f"\nO produto com o maior total de unidades vendidas é: {produto_mais_vendido}")
print(f"Total de unidades vendidas do {produto_mais_vendido}: {maior_quantidade_vendida:.0f}")

# --- Fim da lógica para responder à pergunta ---
