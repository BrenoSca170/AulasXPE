import pandas as pd
import os

# Caminhos dos arquivos
mods_path = r'C:\Users\breno\Desktop\Pycoisas\AulasXPE\Módulo 2\ZomboidModsTESTES\modsMain'
ultralight_path = r'C:\Users\breno\Desktop\Pycoisas\AulasXPE\Módulo 2\ZomboidModsTESTES\modsULTRALIGHT'

# Função pra ler e transformar em coluna
def ler_e_transpor(caminho):
    if not os.path.isfile(caminho):
        raise FileNotFoundError(f'Arquivo não encontrado: {caminho}')
    df = pd.read_csv(caminho, sep=';', encoding='Latin1', header=None).T
    df.columns = ['Valores']
    return df

# Lê os dois arquivos
mods_df = ler_e_transpor(mods_path)
ultralight_df = ler_e_transpor(ultralight_path)

# Converte pra sets (strip pra evitar espaços)
mods_set = set(mods_df['Valores'].astype(str).str.strip())
ultralight_set = set(ultralight_df['Valores'].astype(str).str.strip())

# Comparações
repetidos = sorted(mods_set & ultralight_set)
so_mods = sorted(mods_set - ultralight_set)
so_ultralight = sorted(ultralight_set - mods_set)

# Descobre o maior tamanho
max_len = max(len(repetidos), len(so_mods), len(so_ultralight))

# Preenche com string vazia onde faltar
def pad(lista):
    return lista + [''] * (max_len - len(lista))

# Monta DataFrame
comparacao_df = pd.DataFrame({
    'Repetidos': pad(repetidos),
    'Só no mods': pad(so_mods),
    'Só no modsULTRALIGHT': pad(so_ultralight),
})

# Salva no Excel
comparacao_df.to_excel('comparacao_mods.xlsx', index=False)
