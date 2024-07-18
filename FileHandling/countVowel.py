# wap to count no. of vowels and total number of characters
count=0
f=open('xyz.txt','r')
t=f.read()
vowel=['a','e','i','o','u']
for x in t:
  if x in vowel:
    count+=1
print("the no of vowel is",count)
print("the no of charcaters",len(t))
f.close()
