import pandas as pd
data={'A':[11,12,13,14,15],
      'B':[16,17,18,19,20],
      'C':[21,22,23,24,25]}
df=pd.DataFrame(data,index=['a','b','c','d','e'])
# print the dataframe
print(df)
# Positional indexing using iloc
print(df.iloc[0])
# label based indexing using loc
print(df.loc['b'])
# Booleean slicing
print(df[df['A']>13])
