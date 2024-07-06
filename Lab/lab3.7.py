# WAP to input name of 5 Countries and sort them in ascending order and also in descending order.

a=input("enter 5 countries:").split()
a.sort()
print("ascending Order",a)
a.sort(reverse=True)
print("Descending order",a)