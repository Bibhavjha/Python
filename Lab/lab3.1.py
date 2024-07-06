# WAP to input a sentence and count its number of characters
alpha=0
ch=input("Enter a sentence")
for x in ch:
    if x.isalpha():
        alpha+=1
print("Number of character is",alpha)
