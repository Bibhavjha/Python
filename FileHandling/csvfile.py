import csv
with open("records.txt","w") as csvfiles:
    header=['ID','NAME','AGE','FACULTY']
    data=[[1,"ram",20,'bim'],
          [2,"hari",21,'BIM'],
          [3,'shyam',20,'BCA']]
    csvwriter=csv.writer(csvfiles)
    csvwriter.writerow(header)
    csvwriter.writerows(data)
    csvfiles.close()