import pandas as pd
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', None)
df=pd.read_csv("Data/les-arbres.csv",sep=';')
print(df.describe)

