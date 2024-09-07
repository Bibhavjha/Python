# Write a program to count number of vowels in a string
a=input("Enter a word:")
vowel=('a','e','i','o','u')
count=0
for i in a:
    if i in vowel:
        count+=1
print("total number of vowel",count)
