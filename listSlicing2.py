# WAP to input 5 countries and print them from last to first
countries=input("Enter name of 5 countries").split()
country=countries[-1:-5:-1]
# country=countries[-1:-5:-1]
print(country)