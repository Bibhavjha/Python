# wap to input name of 5 countries and print only those name that began with N
a=input('enter 5 countries:').split()
for x in a:
    if x.lower().startswith('n'):
        print(x)
