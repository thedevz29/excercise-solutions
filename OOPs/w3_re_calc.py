# The question from w3 resource is mentioned below
''' Write a Python program to create a calculator class.
Include methods for basic arithmetic operations.
'''

# Step1: write the class and functions
class Calculator:
    def add(self,x,y):
        return x+y

    def subtract(self,x,y):
        return x-y
    def multiply(self,x,y):
        return x*y
    
    def divide(self,x,y):
        try:
            return x/y
        except ZeroDivisionError:
            return "A problem occured because you put the second value as zero"
        
# Step_2: Give an implementation
        
test_object = Calculator()

print(test_object.add(7,5))

print(test_object.subtract(7,5))


print(test_object.multiply(7,5))


print(test_object.divide(7,5))
