#Getting input more efficiently with lists
#Mr Pinizzotto
#May 12

#how we used to get multiple input
runAgain = input("Do you want to get more info? ")
while runAgain == "yes":
    newThing = input("enter your new item: ")

    runAgain = input("Do you want to get more info? ")
else:
    print("Ok Bye!")

#more efficient (you know how many to get/they are all different)
name, age, favouriteFood = input("Enter your name, age, and favoruite food (separated by space): ").split()
print(name)
print(age)
print(favouriteFood)

#more efficient (you have a lot of input that is the same)
favFoods = list(map(str, input("Enter fav foods (separate with comma): ").split(", ")))
print(favFoods)
