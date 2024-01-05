import pandas as pd
import numpy as np
from datetime import datetime


def valida_numero_tipo_inteiro(df, column):
    mask = df[column].notnull()
    df.loc[mask, column] = pd.to_numeric(df.loc[mask, column], errors="coerce", downcast="unsigned").fillna("ERROR => '" + df.loc[mask, column].astype(str) + "' Motivo => Valor é inválido para o tipo 'Inteiro'")

def valida_tamanho_string(df, column, length):
    mask = df[column].notnull()
    df.loc[mask, column] = df[column].where(df[column].str.len().between(0, length), "ERROR => '" + df[column] + "' Motivo => Excede o tamanho máximo de " + str(length) + " caracteres permitido para o campo")

nome_arquivo = 'dados.csv'
df = pd.read_csv(nome_arquivo, sep=";", names=['A', 'B', 'C', 'D'], skipinitialspace = True)

valida_numero_tipo_inteiro(df, 'B')
valida_tamanho_string(df, 'A', 10)

filtro = df.applymap(lambda x: str(x).startswith("ERROR => "))

df_invalido = df[filtro.any(axis=1)]
df = df[~filtro.any(axis=1)]

tuplas_erros = []
for _, row in df_invalido.iterrows():
    erros = []
    for column in df.columns:
        if str(row[column]).startswith("ERROR => "):
            erros.append(f"Coluna {column}: {row[column]}")
    if erros:
        tuplas_erros.append(
            (
                "Nome da tabela",
                "Nome do arquivo",
                " | ".join(erros),
                datetime.now().isoformat(),
            )
        )


print(df)
print(df_invalido)
print(tuplas_erros)


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
