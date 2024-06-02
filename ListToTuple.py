# a=('apple','mango')
# b=list(a)
# b.append('orange')
# b[0]='cherry'
# a=tuple(b)
# print(a)
a=('apple','orange','mango')
b=list(a)
b.remove('apple')
a=tuple(b)
print(a)
# we can also delete a tuple using del keyword
a=(2,3)
del a
print(a)

