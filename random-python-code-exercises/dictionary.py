#DICTIONARY is used to store values that are in key-value pairs
#DICTIONARY uses curlybraces {}

band=  {
    "vocals": "soprano",
    "guitar": "acoustic",
    "type": "electric"
}

#DICTIONARY uses any data type
print("")
band2 = dict(vocals = "tenor", guitar = "jazz") #using the dict constructor


print(band)
print(band2)

print(type(band))
print(len(band))

#to access items
print(band["vocals"])
print(band["guitar"])
print("")
print(band.get("guitar")) #to output a particular value from the dictionary key.


print("")
#list all keys
print(band.keys())
#list all values
print(band.values())

print("")
#list of key/value pairs as tuple
print(band.items())

#verify the existence of a key
print("")
print("guitar" in band) #output a boolean value to verify the existence of a key in dictionay
print("triangle" in band)
print("vocals" in band)

#change values in a dictionary
band["vocals"] = "HIGHPITCH" #vocals key exist so it changes the value to the new value
also
band.update({"tone": "deep"}) #ADDS A NEW KEY PAIR VALUE
print(band)

#remove values
print("")
print(band.pop("tone")) #it returns what was removed
print("")
print(band)

print("")
#another way to add items
band["signer"] = "jhud" #singer key didnt exist so it adds it to the dictionary pair
print(band)
print("")
print(band.popitem()) #removes the last item that was added and returns it as a tuple
print(band)

#delete and clear
print("")
band["drum"] = "snare"
print(band)
del band["drum"]
print(band)
print("")
band2.clear()#removes the dictionary and returns an empty curly braces
print(band2)
 del band2 #deleted without returning anything entirely

#to make a copy using the constructor function: dict
print("")
band3 = dict(band)
print(band3)

#Nested dictionary
print("")
member1 = {
    "name": "prospa",
    "place": "ohio"
}
member2 = {
    "name": "praise",
    "place": "dalas"
}
band4 = {
    "member1" : "member1",
    "member2" : "member2"
}
print(band4)



##SETS

nums = { 1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
print(type(nums))
print(type(nums2))

#no duplicate
nuns = {1, 2, 2, 3}
print(nuns)

#true is a dupe of 1 and false is a dupe of 0
nuns = { 1, True, 2, False, 3, 4, 0}
print(nuns)

nuns.add(8)
print(nuns)

#add elements from one set to another
morenums = { 4 ,5, 7}
nums.update(morenums)
print(nums)

#you can add update with list tuples and dictionaries too


#merge sets to create a new set
one = {2,3,4}
two = {7,8,0}
newset = one.union(two)
print(newset)

one = {1,2,3}
two={2,3,4}
another = print(one.intersection_update(two))
