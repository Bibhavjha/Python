# WAP to input a character and count its frquency in a file abc.txt
a=input("Enter a character")
count=0
f=open("abc.txt","r")
t=f.read().split()
print(t.count(a))
f.close()
