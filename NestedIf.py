# wap To input marks in 3 subjeccts and calculate total 
# marks,percentage,result (pass/fail) and division
a,b,c=input('enter Marks of subject').split()
S1=int(a)
S2=int(b)
S3=int(c)
t=S1+S2+S3
p=t/3
print("Total marks ",t)
# print("Percentage ",p)
# print("Percentage ",round(p))
print("Percentage ",round(p,2))
if S1>=50 and S2>=50 and S3>=50:
    print("Pass")
    if p>=80:
        print("Distinction")
    elif p>=60:
        print("First Division")
    else:
        print("second division")
else:
    print("Fail")


