import pandas as pd
# Set 100 rows to be displayed
pd.options.display.max_rows=100
df=pd.read_csv('record.csv')
print(df)