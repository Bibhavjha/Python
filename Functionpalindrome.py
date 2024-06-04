# create a function checck() that takes a word as argument and 
# check palindrome or not
def check(a):
    rev=a[-1::-1]
    if rev==a:
     print("palindrome")
    else:
     print("Not palindrome")
a=input("enter a word")
check(a)