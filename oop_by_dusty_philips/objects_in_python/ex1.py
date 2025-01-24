class MyFirstClass:
   def reset(self):
      self.x = 0
      self.y = 0
"""to create an object u instantiate the class and assign it to the object created"""      
p = MyFirstClass()
"""called the reset method one the first object 'p' of the class"""
p.reset()
print(p.x, p.y)
print( " ....... " )
"""explicitly call the method on the class and pass the object as the self argument"""
MyFirstClass.reset(p) # <classname>.<method>(<object)
print(p.x, p.y)


p1 = MyFirstClass() #another object of the same class
p2 = MyFirstClass() #another object of the same class

#dynamic attribute creation and assignment
p1.a = 1 
p2.b = 3
p1.x, p1.y = (4, 5)
p2.a = 6
p2.x, p2.y = (7, 8)

print(p1.x, p1.y, p2.x, p.x, p.y)
print("...............")
print("Dynamic assignment of attributes exercise")
import math

class Point:
   """represents a point in the 2D geometric cordinates"""
   def __init__(self, x=0, y=0):
      """Initializes the position of a new point. The x and y
      cordinates can be specified. If they are not, the point defaults
      to the origin
      """
      self.move(x, y)

   def move(self, x, y):
      """Move the point to a new location in 2D space"""
      self.x = x
      self.y = y

   def reset(self):
      """Reset the point back to the geometric origin: 0, 0"""
      self.move(0, 0)

   def calculate_distance(self, other_point):
      """Calculated the distance from the point to a second point
      passed as a parameter.
      This function usrs the Pythagorean Theorem to calculate the distane
      between the two points. The distance is returned as a float.
      """
      return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y) ** 2)

#instatiating an object
point1 = Point()
point2 = Point()

point1.reset()
point2.move(5,2)
assert point2.calculate_distance(point1) == point1.calculate_distance(point2)
point1.move(3,4)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))


print("...............")
#using the __init__function
class Point:
   def __init__(self, x, y):
      self.move(x, y)
   def move(self, x, y):
      self.x = x
      self.y = y
   def reset(self):
      self.move(0, 0)

point = Point(3, 5)
print(point.x, point.y)
   

