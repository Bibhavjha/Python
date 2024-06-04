# create a function that takes name of some countries as argument and then 
# replace all 'a' with 'p'
def myfunction(countries):
    for i in range(len(countries)):
        a=countries[i].replace('a','p')
        countries[i]=a
    print(countries)
mylist=['Nepal','japan','korea']
myfunction(mylist)

