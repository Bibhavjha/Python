# Create a function that takes a word and check whether it is palindrome or not.
def check(a):
    rev=a[-1::-1]
    if rev==a:
     print("palindrome")
    else:
     print("Not palindrome")
a=input("enter a word")
check(a)