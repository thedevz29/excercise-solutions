#The question is given below
'''Write a Python program to create a person class. 
Include attributes like name, country and date of birth. 
Implement a method to determine the person's age.'''
from datetime import datetime
class Person:
    def __init__(self, name,  country, yob):
        self.name = name
        self.country = country
        self.yob = yob
        
    def tell_age(self):
        year = datetime.now().year
        print(f"{self.name}'s age is {year - self.yob}")
        
test = Person("Atharv", "India", 2011)
test.tell_age()