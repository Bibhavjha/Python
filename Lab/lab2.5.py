# WAP to print the following pattern 
"""
1
12
113
1114
11115
"""

for i in range(1, 6):
    for j in range(1, i+1):
        if j==i:
          print(j)
        else:
           print('1',end='')
     
"""
1
10
101
1010
10101
"""

a= 1
for i in range(1,6):
    print(a)
    if i % 2 == 1:
        a = a * 10
    else:
       a = a * 10 + 1

'''  *
    ***
   *****
  *******
 *********
 '''
sp=5
for i in range(1,10,2):
    for k in range(1,sp+1):
        print(end=' ')
    for j in range (1,i+1):
          print('*',end='')
    print()
    sp=sp-1

