# create a function that takes a list of country names and returns the
# countries that end with vowel
def vowel(countries):
    vowel=('a','e','i','o','u')
    a=[]
    for country in countries:
        if country.lower().endswith(vowel):
         a.append(country)
    return a    
countries=['usa','germany','india','nepal']
print(vowel(countries))