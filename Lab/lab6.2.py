# Write the following menu driven program:
#    1. Write
#    2. Read
#    3. Append
#     Enter your choice:
while True:
 print("1.Write\n2.read\n3.Append")
 num=int(input("Enter your choice:"))

 match num:
    case 1:
        f=open("m.txt",'w')
        f.write(input("Enter you write:"))
        f.close()
    case 2:
        f=open("m.txt",'r')
        print(f.read())
        f.close()
    case 3:
        f=open("m.txt",'a')
        f.write(input("Enter what you want to write"))
        f.close()
    case other:
        print("invalid number")
        break

