n=int(input('Enter a number'))
sum=0
for x in range(1,n+1):
    # It accepts same variable name but is better to use different 
    sum=sum+x
print("the sum is",sum)