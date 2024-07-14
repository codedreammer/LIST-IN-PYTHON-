# there is the ulternate method to change thr tuples 
countries = ("spain","itly","india")
temp = list(countries)
temp.append("russia") #add item
temp.pop(3)           #remove item
temp[2] = "finland"    #change item
countries = tuple(temp)
print(countries)
