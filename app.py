import pandas as pd


nome_arquivo = 'dados.csv'
df = pd.read_csv(nome_arquivo, sep=";", names=['A', 'B', 'C', 'D'])

df['B'] = pd.to_numeric(df['B'], errors='coerce', downcast='integer').fillna('ERROR: O valor ' + df['B'].astype(str) + ' é inválido')
df['D'] = pd.to_datetime(df['D'], errors='coerce').fillna('ERROR: O valor ' + df['D'].astype(str) + ' é inválido')

filtro = df.applymap(lambda x: str(x).startswith('ERROR: O valor'))
novo_df = df[filtro.any(axis=1)].copy()

df = df[~filtro.any(axis=1)]

print("DataFrame com valores válidos")
print(df)
print()

print("DataFrame com valores inválidos")
print(novo_df)
