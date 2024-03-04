import pandas as pd
import numpy as np
from datetime import datetime


def preencher_vazios(elemento):
    if elemento == '':
        return 'campo nao pode ser vazio'
    else:
        return elemento

nome_arquivo = 'dados.csv'
df = pd.read_csv(nome_arquivo, sep=";", names=['A', 'B', 'C', 'D'], skipinitialspace = True, dtype=str, na_filter=False)

# for coluna in colunas:
#     df[coluna] = df[coluna].map(preencher_vazios)
df[['A', 'D']] = df[['A', 'D']].where(df[['A', 'D']] != '', 'campo nao pode ser vazio')
df['B'] = df['B'].where(df['B'] == '', pd.to_numeric(df['B'], errors='coerce', downcast='unsigned').fillna(df['B'] + ' Valor Inválido'))



print(df)