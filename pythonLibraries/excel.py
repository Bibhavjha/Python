import pandas as pd
df=pd.read_excel('employee.xlsx')
# print all data
print(df)
print(df.head())
# print only top 2 rows
print(df.head(2))
# print only last 5 rows
print(df.tail())
print(df.tail(3))
# print data of name column only '
print(df['name'])
# print data of multiple columns
print(df[['name','salary']])
# to remove duplicate records
def1=df.drop_duplicates()
print(def1)
# to fill custom in empty(mssing )cells
df2=df.fillna('missing')
print(df2)
# to drop/remove records with missing values
df3=df.dropna()
print(df3)
