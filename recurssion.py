#recurssions:is when a function calls itself

def add_one(num):
     if (num >=9):
         return num + 1
    
     total = num + 1
     print(total)

     return add_one(total)

newtotal = add_one(0)
print(newtotal)


#square=[]
#or i in range(10):
#    squared =i*i
#    square.append(squared)
#   print(square)


