# to input a number and find its factorial
def fact(n):
    if n==1:
     return 1
    else:
       return n*fact(n-1)
n=int(input('enter a number'))
print('factorial is',fact(n))
   