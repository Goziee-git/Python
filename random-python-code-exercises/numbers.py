#numeric datatype integers
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, bool))

print("")
#floating type
gpa = 1.34
y = float(45.5)
print(type(gpa))

#complex numbers
comp_value = 5+4j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)
# #built in functions for numbers
# print(abs(gpa)) ##absolute value built_in function
# print(round(gpa)) #round to the nearest integer
# print(round(gpa, 1)) #round to the nearest number specified

# ##using modules, usually are done at the top of the file
# import math 
# print(math.pi)
# print(math.sqrt(64))
# print(math.ceil) ##rounde up
# print(math.floor) ##rounded down