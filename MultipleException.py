# Wap to handle multiple error
try:
 a=int(input('enter first number'))
 b=int(input('enter second number'))
 c=a/b
 print('result=',c)
except ValueError as ve:
   print(ve)
except ZeroDivisionError as ze:
  print(ze)