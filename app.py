import pandas as pd
import numpy as np


def converter_data(value):
    try:
        value = pd.to_datetime(value, format="%Y%m%d")
        return value
    except:
        return "Data inválida"

nome_arquivo = 'dados.csv'
df = pd.read_csv(nome_arquivo, sep=";", names=['A', 'B', 'C', 'D'], skipinitialspace = True)
df = df['D'].apply(converter_data)

print(df)


# df = df.where(pd.notnull(df), None)
# for column in df.columns:
#     if df[column].dtype == object:
#         df[column] = df[column].str.strip()

# df['B'] = df['B'].str.strip()
# mask = df['B'].notnull()
# df.loc[mask, 'B'] = pd.to_numeric(df.loc[mask, 'B'], errors='coerce', downcast='integer').fillna('ERROR: O valor ' + df.loc[mask, 'B'].astype(str) + ' é inválido')


# mask = df['D'].notnull()
# df.loc[mask, 'D'] = pd.to_datetime(df.loc[mask, 'D'], format="%Y/%m/%d", errors="coerce").fillna("ERROR: O valor " + df['D'].astype(str) + " é inválido")

# filtro = df.applymap(lambda x: str(x).startswith('ERROR: O valor'))
# novo_df = df[filtro.any(axis=1)].copy()

# df = df[~filtro.any(axis=1)]

# print("DataFrame com valores válidos")
# print(df)
# print()

# print("DataFrame com valores inválidos")
# print(novo_df)
