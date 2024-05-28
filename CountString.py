# WA
space=0
alpha=0
digit=0
word=0
a=input("Enter a sentence ")
for x in a:
  if x.isspace():
   space+=1
  elif x.isalpha():
   alpha+=1
  elif x.isdigit():
   digit+=1
print("space",space,"alphabet",alpha,"digit",digit,"word",space+1)