import pandas as pd
import numpy as np
from datetime import datetime


nome_arquivo = 'dados.csv'
df = pd.read_csv(nome_arquivo, sep=";", names=['A', 'B', 'C', 'D'], skipinitialspace = True)

print(df)