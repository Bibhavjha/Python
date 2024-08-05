import pandas as pd
data={
    'ID':[101,102,103,104,105],
    'Name':['Ram','Hari','Sita','Rita','Ravi'],
    'Age':[25,24,26,27,25],
    'Salary':[25000,24000,26000,27000,25000]
}
df=pd.DataFrame(data)
df.to_csv('record.csv',index=False)

# appending to a csv file
data={
    'ID':[106,107],
    'Name':['puja','Rajeev'],
    'Age':[20,21],
    'Salary':[20000,21000]
}
df=pd.DataFrame(data)
df.to_csv('record.csv',mode='a',header=False,index=False)

# reading a CSV file
import pandas as pd
df=pd.read_csv('record.csv')
print(df)
# use to_string() to print the entire Dataframe
print(df.to_string())