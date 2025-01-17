a=100
def func_scope():
   global a #a  deined outside the function is global
   print('here a is ', a)
   a = 20
   print('a here is now ',a)
a = 30 #a defined here will be used instead of above and outside
func_scope()

print("the value of a here is now", a)
#Nonlocal statement
print(" ............... ")
def outside():
   a = 100
   def inside():
      nonlocal a
      a = 20
      print("inside value of a", a)
   inside()
   print("ouside value of a",a)
outside()