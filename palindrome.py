a=int(input("Enter a number"))
n=a
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if a==rev:
    print("it is palindrome")
else:
    print("not palindrome")