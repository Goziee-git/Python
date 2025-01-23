
"""importing a module from a package"""
import my_package.module1
print(my_package.module1.MY_VAR)
my_package.module1.my_function()
my_package.module1.MyClass()

print( " .............. ")

"""importing a function a variable and a class from a module in a package"""
from my_package.module1 import my_function, MY_VAR, MyClass
my_function()
print(MY_VAR)
MyClass()

print( "............. ")
"""importing a submodule from a package"""
import my_package.submodule.submodule1
print(my_package.submodule.submodule1.MY_SUB_VAR)
my_package.submodule.submodule1.my_sub_function()

print( "............. ")
"""importing a function and a variable from a submodule in a package"""
from my_package.submodule.submodule1 import MY_SUB_VAR, my_sub_function
my_sub_function()
print(MY_SUB_VAR)

print( "............. ")
"""we can also import a package"""
import my_package
print(my_package.module1.MY_VAR)

print( "............. ")
"""importing a class from a module of a subpackage inside a package"""
from my_package.package_02.module02_1 import MyClass
MyClass()

print( "............. ")
"""doing lazy imports, importing directly from a function defined in the __init__.py file"""
from my_package.submodule import get_my_class()
MyClass = get_my_class()

