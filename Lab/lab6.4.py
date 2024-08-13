# Read from "emp.csv" and display all records.
import pandas as pd
# Set 100 rows to be displayed
pd.options.display.max_rows=5
df=pd.read_csv('emp.csv')
print(df)

