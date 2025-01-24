class Student:
   def __init__(self, name, score):
      self.name = name
      self.__score = score

   def student_info(self):
      print(f"Name {self.name}, Score: {self.__score}")

   def get_score(self):
      return self.__score

   def get_name(self):
      return self.name

   def pass_fail(self, score):
      if score > 50:
         self.__score = score
      else:
            print("WORK HARDER NEXT TIME")

Prospa = Student("prospa", 80)
print(Prospa.get_name())
print(Prospa.get_score())
Prospa.student_info()
Glory = Student("Glory", 30)
print(Glory.get_name())
print(Glory.get_score())
Glory.student_info()
try:
   print(Student.__score) ##without the try-exception block will raise AttributeError becos we cant access private attrubute
except AttributeError as ae:
   print(ae)
"""accessing the private attribute using name mangling
|<print>(<Object_name>._<class_name>__<private_attribute_name>)
"""
print(".......................")
print(Prospa._Student__score)
print(Glory._Student__score)
print("..........................")
"""using the pass_fail method to modify the private __score attribute"""
Prospa.pass_fail(100)
print(Prospa.get_score())
Prospa.student_info()