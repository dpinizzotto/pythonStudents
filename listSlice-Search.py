#List Slicing and searching
#Mr Pinizzotto
#May 6

#create a list of food items
foodList = ["pizza", "tater tots", "wings", "sandwich", "falafel", "taco", "fries", "wings"]

#regular printing
print(foodList)

#print first 3 (top 3) items
print(foodList[:3])

#print middle items give start, and end (not including)
print(foodList[2:5])

#everything but first
print(foodList[1:])

#print every other one
print(foodList[0:6:2])
print(foodList[1:6:2])

print()
print()
#check for doubles
for x in range(len(foodList)):
    #set the current spot as the search item
    dupe = foodList[x]
    #looked in the rest of the list
    if dupe in foodList[x+1:]:
        print("Duplicate found!")


print()
print()
while(True):
    searchItem = input("Which food do you want to look for in the list?").lower()

    if searchItem in foodList:
        print("Yes it is in the list!!")
    else:
        print("Not in the list")


    


