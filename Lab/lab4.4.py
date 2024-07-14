# WAP to find factorial of a number using recursive.
def fact(n):
    if n==1:
     return 1
    else:
       return n*fact(n-1)
n=int(input('enter a number'))
print('factorial is',fact(n))