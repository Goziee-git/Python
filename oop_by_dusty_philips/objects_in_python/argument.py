#HOW DO WE PASS MORE ARGUMENTS TO THE METHOD?
class HelloWorld:
   """Add more parameters to the method definition"""
   def mymethod(self, arg1, arg2):
      print(f"Argument1: {arg1}")
      print(f"Argument2: {arg2}")
Word1 = HelloWorld()
Word1.mymethod("Hello", "World")
Word1.arg1, Word1.arg2 = "Hello", "World"
print(Word1.arg1, Word1.arg2)

print("..............")
#USING KEY WORD ARGUMENTS
class HelloWorld:
   """arguments as keyword arguments"""
   def my_method(self, arg1, arg2, key="Python"):
      self.arg1 = arg1
      self.arg2  = arg2
      self.key = key
      print(f"argument1:{self.arg1}")
      print(f"argument2:{self.arg2}")
      print(f"argument3:{self.key}")
      return self

obj = HelloWorld(); obj.my_method("Hello", "world", key="Word"); print(obj.arg1,obj.arg2,obj.key)
obj = HelloWorld().my_method("Hello", "World", key="Python")
print(obj.arg1, obj.arg2, obj.key)

print("..............")
print("Dynamic attribute assignment using srtattr")
#USING VARIABLE LENGTH POSITIONAL ARGUMENTS(*args)
class Class:
   """this case uses the setattr to dyanmically set attributes to the object using 
   method with unknown positional arguments"""
   def my_method(self, *args):
      for ag, arg in enumerate(args):
         print(f"Argument {ag+1}: {arg}")
         """we use setattr to dynamically assign the attributes to the object"""
         setattr(self, f"arg{ag+1}", arg)
      return self

obj = Class().my_method("Hello", "World", "Python"); print(obj.arg1, obj.arg2, obj.arg3)

print("................. ")
pront("Dynamically assign and print using __dict__ attribute of object")
#Dynamically assign and print attributes using the __dict__ attribute of an object
class Class:
   def my_method(self, *args):
      for i, arg in enumerate(args):
         setattr(self, f"arg{i+1}", arg)
      return self
   def print_args(self):
      for key,value in self.__dict__.items():
         print(f"{key}: {value}")
         """Note here that: the __dict__ attributes holds all the attributes of an object as 
         a key value pair dictionary"""

obj = Class().my_method("Hello", "World", 1, 2, 3); obj.print_args()

print("................. ")
print("Dynamically assign and print using getattr")

class Class:
    def my_method(self, *args):
        for i, arg in enumerate(args):
            setattr(self, f"arg{i+1}", arg)
        return self

    def print_attributes(self):
        i = 1
        while True:
            attr_name = f"arg{i}"
            if hasattr(self, attr_name):  # Check if the attribute exists
                print(f"{attr_name}: {getattr(self, attr_name)}")
                i += 1
            else:
                break  # Stop when no more attributes are found

# Create instance, call method, and print attributes
obj = Class().my_method("Hello", "World", "Python")
obj.print_attributes()
