# WAP to input name of 5 countries and print only those which start with “N”.
a=input('enter 5 countries:').split()
for x in a:
    if x.upper().startswith('N'):
        print(x, end=' ')
