# WAP to input marks in 5 subjects and then calculate total marks, percentage, division and result(pass/fail)
a,b,c,d,e=input('enter Marks of subject').split()
S1=int(a)
S2=int(b)
S3=int(c)
S4=int(d)
S5=int(e)
t=S1+S2+S3+S4+S5
p=t/5
print("Total marks ",t)
# print("Percentage ",p)
# print("Percentage ",round(p))
print("Percentage ",round(p,2))
if S1>=50 and S2>=50 and S3>=50 and S4>=50 and S5>=50:
    print("Pass")
    if p>=80:
        print("Distinction")
    elif p>=60:
        print("First Division")
    else:
        print("second division")
else:
    print("Fail")


