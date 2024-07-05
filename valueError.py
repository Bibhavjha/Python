# wap to handle valueError 
try:
 a=int(input('enter first number'))
 b=int(input('enter second number'))
 c=a+b
 print('result=',c)
except ValueError as ve:
   print(ve)