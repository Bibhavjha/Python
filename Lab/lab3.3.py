# WAP to input a sentence and count the number of vowels.
count=0
a=input('Enter a sentence:')
b=a.lower()
vowels=['a','e','i','o','u']
for x in b:
  if x in vowels:
    count+=1
print("the no of vowel is",count)
