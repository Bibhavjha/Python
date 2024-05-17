#To input a number and find its factorial
a=int(input("Enter a number"))
factorial=1
for x in range(1,a+1):
    factorial=factorial*x
print("The factorial of given number is",factorial)
  