# create a function that takes two numbers a and b and return
# sum of a and reverse value of b
def sum(a,b):
    sum=0
    while b>0:
        r=b%10
        sum=sum*10+r
        b=b//10
    return a+sum
print(sum(5,12))