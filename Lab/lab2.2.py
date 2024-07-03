# WAP to input a number and print all of its digits. Also find the sum of all digits.
a=int(input("Enter a number:"))
sum=0
while a>0:
    r=a%10
    print(r)
    sum=sum+r
    a=a//10
print(sum)
    
