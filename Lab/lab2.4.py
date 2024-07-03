# WAP to print all prime numbers from a to b where a and b are taken as input from user.
a=int(input("Enter first number"))
b=int(input("Enter second number"))
for i in range(a,b+1):
    count=0
    for x in range(1,i+1):
        if i%x==0:
            count+=1
    if count==2:
        print(i,end=' ')
