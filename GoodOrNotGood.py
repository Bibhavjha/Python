'''a number is a good number if it contains equal no of
digits 0 and 1.WAP to input a number and check whether it is 
a good number or not
Eg: 123->good number,1023->not good,11023->not good'''
c1=0 #for Zero
c2=0 #for One
n=int(input('Enter a number'))
while n>0:
    if n%10==0:
        c1+=100
    elif n%10==1:
        c2+=1
    n=n//10
if c1==c2:
    print("good number")
else:
    print("not good number")
