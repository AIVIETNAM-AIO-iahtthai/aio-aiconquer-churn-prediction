path = r'C:/Users/Admin/Downloads/churndata.csv'
import pandas as pd
df = pd.read_csv(path,sep=';')
df = pd.DataFrame(df)
print(df)