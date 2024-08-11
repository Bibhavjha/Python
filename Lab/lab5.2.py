# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
import datetime as dt
class person:
    def __init__(self,name,country,DOB):
        self.name=name
        self.country=country
        self.DOB=DOB
    def age(self):
        age=datetime.today()-self.DOB
        print(age)
p=person("Ram","Nepal","8/10/2024")
p.age()
        
       