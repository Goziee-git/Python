#SETS (unordered,unchangeable,no-duplicates,unindexed)

name = {'prosper', 1,3,False}
print(name)

names = set(("mee",2,True,0))
print(names)
print(type(name))
print(False in name)
print(1 not in name)
#add to set
name = {'pee',"you","mee","tim"}
age = {10,20,30}
city = {"willis","jico",30,"storm"}
print(name)
name.add("tom")
print(name)#tom added
city.update(name)
print(city)#use update method to add any iterable
city.remove("jico")
print(city)
city.discard("storm")
city.pop()
print(city)
city_age = city.union(age)
print(city_age)
city.update(name)
print(city)
in_both = city.intersection(age)
print(in_both)
city.difference_update(age)
print(city)