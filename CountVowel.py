# wap to insert a word and count the no of vowels
count=0
a=input('Enter a word')
b=a.lower()
vowels=['a','e','i','o','u']
for x in b:
  if x in vowels:
    count+=1
print("the no of vowel is",count)
