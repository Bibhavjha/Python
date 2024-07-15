# WAP to multiply two number by using recursive function.
def mul(a,b):
    if a==0 | b==0:
        return 0
    elif a==1:
        return b
    elif b==1:
        return a
    else:
        return a+mul(a,b-1)
print(mul(0,1))