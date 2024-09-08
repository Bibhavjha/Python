# write a program to check entered number is prime or not 
a=int(input("Enter a number: "))
c=0
for x in range(1,a+1):
    if a%x==0:
        c+=1
if c==2:
    print(a,"is prime")
else:
    print(a,"is composite")
