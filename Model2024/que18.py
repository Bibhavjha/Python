# example of match case 
a=int(input("Enter number between 1-7: "))
match a:
    case 1:
        print("today is sunday")
    case 2:
        print("today is monday")
    case 3:
        print("today is tuesday")
    case 4:
        print("today is wednusday")
    case 5:
        print("today is thursday")
    case 6:
        print("today is friday")
    case 7:
        print("today is saturday")
    case other:
        print("Invalid choice")
