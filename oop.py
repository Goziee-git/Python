class myclass: #use the class attribute to create a class
   x = 5

p1 = myclass() #p1 is an instance of the class(myclass)
print(p1.x)  #it makes use of the x property of the class.

class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def greet(self):
      print(f"Hello, My name is {self.name} and i am {self.age} years old")

p1 = Person("John", 21)

print(p1.name)
print(p1.age)
p1.greet()

#using the __str__function

class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def __str__(self):
      return f"{self.name}{self.age}"

p1 = Person("John", 28)
print(p1)

#objects can also have functions, these func are methods that belong to the object

class Animals:
   def __init__(mypets, name, color, age):
      mypets.name = name
      mypets.color = color
      mypets.age = age

   def myfunc(mypets):
      print(f"{mypets.name} is a {mypets.color} puppy, he is {mypets.age} years old")

p1 = Animals("Lenny", "Black", 10)
print(p1.name)
print(p1.color)
print(p1.age)
print(p1)
p1.myfunc()
print(' ........ ')
#attribute reference can also be used to access the attributes of a class
class Person:
   def __init__(self, name, age):
      self.name = name  #instance attributes
      self.age = age

   origin = "African American" #class attibutes

   def personality(self): #instance method
      return f"{self.name} says Igoche"
   def behaviour(self):
      return f" {self.name} is a good person"
   
   @classmethod #class method
   def fromimages(cls,name,age):
      return cls(age)

#creating an instance of the Person class usinig the instance attribute
igbo_man = Person("Chinedu",30)
print(f"this igboman is named", {igbo_man.name})
print(f"this person is aged", {igbo_man.age})

#accessing the class attributes using attribute reference (.dot notation)
print(Person.origin)
#accessing the instance attributes using attribute reference (.dot notation)
print(igbo_man.age)
print(igbo_man.name)

#calling an instance method
print(igbo_man.personality())
print(" .......... ")
#creating an instance of the person class using the class attribute(origin)
another_person = Person("Emeka", 25)
print(f"this person is named {another_person.name} and is {another_person.age} years old")
#creating an instance using the class method
my_igboman = Person.fromimages("chijindu", 40)
print(my_igboman)
#accessing the class attribute
print(Person.origin)
#calling a class method
print(my_igboman.fromimages(21))



