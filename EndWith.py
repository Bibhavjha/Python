# wap to input name of 5 countires and print only that end with a vowel
a=input("enter 5 countries:").split()
vowel=("a","e","i","o","u")
for x in a:
    if x.lower().endswith(vowel): #we can pass tuple in ends with and , is used as or
      print(x)