class MyFirstClass:
   def reset(self):
      self.x = 0
      self.y = 0
"""to create an object we instantiate the class and assign it to the object created"""      
p = MyFirstClass()
"""called the method one the object 'p' of the class"""
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


