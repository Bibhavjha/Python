# Create a csv file "emp.csv" to store id, name, address, salary of 5 employees.
import csv
with open("emp.csv","w") as csvfiles:
    header=['Id','Name','Address','Salary']
    data=[[1,"ram",'KTM',25000],
          [2,"hari","BKT",19000],
          [3,'shyam',"PKR",36000],
          [4,'Sita','BRT',40000],
          [5,'Gita','Nepalgunj',36000]]
    csvwriter=csv.writer(csvfiles)
    csvwriter.writerow(header)
    csvwriter.writerows(data)
    csvfiles.close()