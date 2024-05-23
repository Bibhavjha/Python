'''
create the following menu Driven program
1.Add
2.Subtract
3.Multiply
4.Divide
5.Exit
'''
while(True):
     print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
     choice=int(input("Enter your choice(1-5): "))
     a=int(input("Enter First number "))
     b=int(input("Enter Second number "))
     match choice:
        case 1:
           c=a+b
           print('result=',c)
        case 2:
          c=a-b
          print('result=',c)
        case 3:
          c=a*b
          print('result=',c)
        case 4:
          c=a/b
          print('result',c)
        case 5:
          break
        case other:
           print("Inavlid choice")
        