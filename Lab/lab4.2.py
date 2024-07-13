# Create a function that takes a list of 5 country names and then return only those countries that start with ‘N’.
def WithN(countires):
    a=[]
    for country in countires:
        if country.lower().startswith('n'):
            a.append(country)
    return a
countries=['Nepal','USA','Germany','Nigeria','Iran']
print(WithN(countries))
