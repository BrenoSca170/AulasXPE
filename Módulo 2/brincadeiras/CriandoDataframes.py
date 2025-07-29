import pandas as pd
import numpy as np

dados = np.array([
    ['Breno', 'Carne', np.random.randint(1, 6), np.round(np.random.uniform(10.0,45.0),2)],
    ['Daniele', 'macarrão', np.random.randint(1, 6), np.round(np.random.uniform(10.0,45.0),2)]
])
dict_mercado = {
    'Nome': ['Breno', 'Daniele'],
    'Comida': ['Carne', 'macarrão'],
    'Quantidade': [np.random.randint(1, 6), np.random.randint(1, 6)],
    'Preço': [np.round(np.random.uniform(10.0, 45.0), 2), np.round(np.random.uniform(10.0, 45.0), 2)]
}
df = pd.DataFrame(dados, columns=['Nome', 'Comida', 'Quantidade', 'Preço'])
df1 = pd.DataFrame(dict_mercado)
with pd.ExcelWriter('Clientes.xlsx') as f:
    df.to_excel(f, index=False, sheet_name='Clientes')

    df1.to_excel(f, index=False, sheet_name='Mercado')
