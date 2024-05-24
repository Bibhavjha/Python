# WAP to input a word and check whether it is a plaindrome or not
a=input("enter a word ")
rev=a[-1::-1]
if rev==a:
    print("palindrome")
else:
    print("Not palindrome")