# WAP to input a line of text, store in a file and then read from the file to display its content.
f=open('xyz.txt','w')
f.write(input("Enter a sentence"))
f.close()
f=open('xyz.txt','r')
print(f.read())
f.close()