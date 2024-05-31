# city=['ktm','bkt','pkr','brt']
# city.sort(key=str.lower)
# print(city)
# wap to sort name of cities without using sort() method
cities=input("enter name of  5 cities :").split()
for i in range(0,5):
    for j in range(i+1,5):
        if cities[i]>cities[j]:
            temp=cities[i]
            cities[i]=cities[j]
            cities[j]=temp
print(cities)