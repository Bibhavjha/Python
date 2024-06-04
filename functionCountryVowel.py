def vowel(country):
    vowel=('a','e','i','o','u')
    countries=[]
    for i in country:
        if country.endswith(vowel):
            countries.append(country)
    return country
country=['usa','india','nepal']
print(vowel(country))
