# wap to input a word and total number of frequency in afile abc.txt
a=input("Enter a word")
count=0
f=open("abc.txt",'r')
t=f.read().split()
print(t.count(a))
f.close()