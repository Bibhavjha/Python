day=int(input("Enter a day number "))
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednusday")
    case 5:
        print("Thursday")
    case 5:
        print("Friday")
    case 7:
        print("Saturday")
    case _: #we can use case_ instead of case Other 
        print("Invalid day")
    