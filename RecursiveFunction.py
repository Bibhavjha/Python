# to print 1-50 using recursive function
def numbers(n):
    if n<=50:
        print(n,end=' ')
        numbers(n+1)
numbers(1)
# in reverse 
def numbers(n):
    if n<=50:
        numbers(n+1)
        print(n,end=' ')
numbers(1)
