try:
 a=int(input('enter first number'))
 b=int(input('enter second number'))
 c=a//b
 print('result=',c)
except (ValueError,ZeroDivisionError) as e:
       print(e)
     
  