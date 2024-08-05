import pandas as pd
data1={'Name':['ram','sita','hari'],'Age':[21,20,22]}
data2={'City':['ktm','bkt','pkr']}

df1=pd.DataFrame(data1,index=['A','B','C'])
df2=pd.DataFrame(data2,index=['B','C','D'])

# join using left- Left join
df3=df1.join(df2,how='left')
print(df3)

# join using right -Right Join
df4=df1.join(df2, how='right')
print(df4)