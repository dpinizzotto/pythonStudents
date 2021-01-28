#List Methods
#Mr Pinizzotto
#May 8, 2020

#set up my list, to be filled later
gamesList = []


#get the user to input the values of their list
while True:

    #ask them to input the list of games they have played/beaten
    #over quarantine
    #append adds to the back of the list
    gamesList.append(input("Enter a game you have beat/played since March 13: "))

    #old way
    #game = input("Enter a game you have beat/played since March 13: ")
    #gamesList.append(game)

    #ask a question to break the loop
    endLoop = input("Do you have more to add? ").lower()

    if endLoop == "n" or endLoop == "no":
        break

#finish loop print
print()
print(gamesList)

#print sorted list
print("\n Sorted List")
#sort first
gamesList.sort()
print(gamesList)

#print reversed list
print("\n Reverse order List")
#sort first
gamesList.reverse()
print(gamesList,"\n")

#how to remove
removeThing = input("Do you have an item to remove? ").lower()
while removeThing == "yes" or removeThing == "y":
    #ask for the item
    removeItem = input("What game do you want to remove? ").lower()
    if removeItem in gamesList:
        gamesList.remove()
    else:
        print("Error, item not in the list")

    removeThing = input("Do you have an item to remove? ").lower()



#finish loop print
print("\n New List")
print(gamesList)
