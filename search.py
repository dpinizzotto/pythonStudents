#gather the name that the user is looking for
search = input("Enter the name you want to find")

#create the array with the names in it
names = ["Doug", "Rob", "Martin", "Jozy"]

#check if the name is in the array
if search in names:
    print("Name Found")
else:
    print("Name not in list")


#have a variable that determines if the name was found for the end print if
#it is not found
nameFound = False

#loop from 0 to the end of the array, len(names) gives the end point
for x in range(len(names)):

    #checking at each element
    if search == names[x]:
        print("Name Found!!")
        #changes the end print
        nameFound = True
        #once the name is found, we do not need to loop
        break

#end print if we went through the loop unsuccessfully
#if we didn't have this it would always print
if nameFound == False:
    print("Name not in list")

        

