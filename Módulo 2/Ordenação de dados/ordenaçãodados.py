import pandas as pd
import numpy as np

# dados = {
#     'Nome': [
#         'Maria', 'João', 'Ana', 'Pedro', 'João',
#         'Lucas', 'Julia', 'Carlos', 'Beatriz', 'Fernanda',
#         'Tiago', 'Clara', 'Marcos', 'Larissa', 'Rafael',
#         'Sofia', 'Bruno', 'Isabela', 'Gustavo', 'Camila',
#         'Maria', 'João', 'Ana', 'Pedro', 'Lucas',
#         'Julia', 'Carlos', 'Beatriz', 'Fernanda', 'Tiago',
#         'Clara', 'Marcos', 'Larissa', 'Rafael', 'Sofia',
#         'Bruno', 'Isabela', 'Gustavo', 'Camila', 'João'
#     ],
#     'Categoria': [
#         'A', 'B', 'A', 'B', 'B',
#         'C', 'A', 'C', 'B', 'A',
#         'C', 'A', 'B', 'C', 'B',
#         'A', 'C', 'B', 'A', 'C',
#         'B', 'A', 'C', 'B', 'A',
#         'B', 'A', 'C', 'B', 'A',
#         'C', 'A', 'B', 'C', 'A',
#         'B', 'C', 'A', 'C', 'B'
#     ],
#     'Vendas': [
#         100, 200, 150, 250, 350,
#         180, 300, 120, 220, 310,
#         400, 210, 230, 170, 260,
#         290, 330, 240, 280, 360,
#         190, 215, 140, 270, 185,
#         310, 110, 205, 315, 390,
#         250, 195, 235, 175, 285,
#         320, 255, 275, 365, 225
#     ],
#     'Qtd_Vendas': [
#         2, 4, 2, 2, 4,
#         2, 2, 2, 2, 2,
#         2, 2, 2, 2, 2,
#         2, 2, 2, 2, 2,
#         2, 4, 2, 2, 2,
#         2, 2, 2, 2, 2,
#         2, 2, 2, 2, 2,
#         2, 2, 2, 2, 4
#     ]
# }

# df = pd.DataFrame(dados)

### GROUP BY

# grouped = df.groupby('Categoria')
# feito = grouped.agg(
#     Total_vendas = ('Vendas','sum'),
#     Média_vendas = ('Vendas','mean'),
#
# )
#
# print(feito)

### PIVOT TABLE

# df_pivot = df.pivot_table(index='Categoria', columns='Nome',values='Vendas',aggfunc='sum')
# print(df_pivot.head())

### CROSS TAB ###
#
# breno = pd.crosstab(df['Categoria'], df['Nome'])
# print(breno)

### INFO ###
#
# print(df.describe().transpose())

### ASSIGN c/ LAMBDA ###
#
# df = df.assign(Vendas_menos_juros = lambda x: 1.9* x['Vendas'] )
# print(df.head())

### TRANSFORM ###
#
# df['Média_Grupo'] = df.groupby('Categoria')['Vendas'].transform('mean')
# print(df.head())

### APPLY ###

# df['resultado'] = df.apply(lambda row: row['Vendas'] * row['Qtd_Vendas'], axis = 1)
#
# def verifica_resultado(resultado):
#     if resultado >= 800:
#         return 'vendas acima do esperado'
#     else:
#         return 'Vendas abaixo do esperado'
#
# df['Avaliação de vendas'] = df['resultado'].apply(verifica_resultado)
# print(df.head())


# DataFrame com mais pessoas
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Nome': ['João', 'Maria', 'Pedro', 'Leandro', 'Ana', 'Lucas', 'Bruna', 'Carlos'],
    'Idade': [25, 30, 28, 32, 22, 29, 27, 31]
})

# DataFrame com mais profissões (incluindo alguns IDs que não estão no df1)
df2 = pd.DataFrame({
    'ID': [1, 2, 5, 6, 8, 9, 10],
    'Profissão': ['Engenheiro', 'Advogado', 'Médico', 'Professor', 'Designer', 'Arquiteto', 'Analista']
})
df1 = pd.DataFrame(df1)
df2 = pd.DataFrame(df2)

### INNER JOIN ###
# df_inner_id = pd.merge(df1, df1, on='ID', how='inner')
#
# print(df_inner_id)
### OUTER JOIN ###
# df_inner_id = pd.merge(df1, df1, on='ID', how='outer')
#
# print(df_inner_id)
### LEFT JOIN ###
# df_inner_id = pd.merge(df1, df1, on='ID', how='left')
#
# print(df_inner_id)
### RIGHT JOIN ###
# df_inner_id = pd.merge(df1, df1, on='ID', how='right')
#
# print(df_inner_id)
### JOIN ###
# df_inner_set = df1.set_index('ID').join(df2.set_index('ID'), how='inner')
# print('Junção inner')
# print(df_inner_set)
# df_inner_set = df1.set_index('ID').join(df2.set_index('ID'), how='outer')
# print('Junção outer')
# print(df_inner_set)
