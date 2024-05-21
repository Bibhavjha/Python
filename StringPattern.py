'''
N
NE
NEP
NEPA
NEPAL
'''
# w='NEPAL'
# for i in range(0,5):
#     for j in range(0,i+1):
#           print(w[j],end='')
#     print()

'''
KATHMANDU
  KATHMAN
   KATHM
    KAT
     K'''
w='KATHMANDU'
sp=1
for i in range(8,-1,-2):
    for k in range(1,sp+1):
          print(end=' ')
    for j in range(0,i+1):
         print(w[j],end='')
    print()
    sp=sp+1
    