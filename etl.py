import pandas as pd
import os
import glob
# uma funcao de extract que le e consolida os json


pasta = 'data'
arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
df_list = [pd.read_json(arquivo) for arquivo in arquivos_json] 
print(df_list)

# uma funcao que transforma os dados

# uma funcao que da load em csv ou parquet

