


def greeting(name=None, greet=None):
   if name is None:
      name = "Nana"
   if greet is None:
      greet = "Hello"
   print(f"GREETING: {greet},my name is {name}")

greeting()
greeting("prospa")
greeting(name="john",)

print(".....................")

def name(lastname, firstname=None):
   if lastname is not None:
      lastname = "Anyanwu"
   if firstname is not None:
      firstname = "prospa"
      print (f"Hello, Fullname is {firstname} {lastname}")
name("mike")
name("Prospa")
name("prospa", "Daniel")
print("  ......................................... ")
"""using a nested class, create an object of the class and call the function"""

def bio(name=None, age=None, origin=None):
   class Biography:

      """define attributes of the class accessed by objects created from the class"""
      def __init__(self, name, age, origin):
         self.name = name if name else "Guest"
         self.age = age
         self.origin = origin if origin else "Nigeria"

      def display_bio(self):
         print(f"Name: {self.name}, \nAge: {self.age}, \norigin: {self.origin}")

   #create an instance of the class and returns the object   
   return Biography(name, age, origin)
#<name_of_object> = <name_of_function>(<arguments>)
african = bio("Prospa", 35, "Nigerian")
african = bio()
african.display_bio()


