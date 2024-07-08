# Wap to handle IndexError
countries=['nepal','india','china','argentina','portugal']
i=int(input('enter the index'))
try:
    print("country at index",i,'is',countries[i])
except IndexError as ie:
    print(ie)