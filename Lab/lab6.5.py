# Read from "emp.csv" and display records of only those whose salary is more than 35000
import pandas as pd
# Set 100 rows to be displayed
pd.options.display.max_rows=5
df=pd.read_csv('emp.csv')
result = df[df['Salary'] > 35000]
print(result)
