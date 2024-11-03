#Question is mentioned below
'''Write a Python program to create a class representing a Circle. 
Include methods to calculate its area and perimeter.'''


class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def circumference(self):
        print(f"The circumference of the circle is {2*3.14*self.radius}")

    def area(self):
        print(f"The area of the circle is {3.14*self.radius**2}")
        
    
object_1 = Circle(7)
object_1.circumference()
object_1.area()
