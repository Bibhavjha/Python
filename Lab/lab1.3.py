# 3.Create the following menu driven program:
# a)Area of circle
# b)Vowel/consonant
# c)Odd/Even
print("1)Area of circle\n 2)vowel/consonant\n 3)odd/even")
x=int(input("Enter your choice"))
match x:
    case 1:
        r=float(input("enter radius of circle:"))
        print("The area of circle is:",3.14**r)
    case 2:
        a=int(input("Enter a letter:"))
        vowel=('a','e','i','o','u')
        if a in vowel:
            print(a,"is vowel")
        else:
            print(a,"is consonant")
    case 3:
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(num,"is even")
        else:
            print(num,"is odd")
    case other:
        print("Your choice is invalid")

