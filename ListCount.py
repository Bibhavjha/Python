# WAP to input a string and count the frequency of 'a'
sent= input("Enter  a sentence ")
print(sent.count('a'))

# wap to input a string and count the frequency of all the characters
sent=input("Enter a string ")
chars=[]
for ch in sent:
    if ch not in chars:
        chars.append(ch)
for ch in chars:
    print(ch,':',sent.count(ch))
