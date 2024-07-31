import pandas as pd
data1={'StudentID':[101,102,103],'Name':['Ram','Hari','Sita']}
data2={'StudentID':[101,102,104],'City':['Ktm','bkt','Pkr']}

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

# merge using inner-Inner join
df3=df1.merge(df2,on='StudentID',how="right")
print(df3)