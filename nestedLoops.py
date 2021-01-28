userInput = input("Shall we continue the program once more")

userInput = userInput.lower()

while userInput == "yes":
    userNumber = int(input("Enter a number to mulitply"))
    for x in range(7):
        print(x,"x",userNumber,"=",x*userNumber,"\n")
    userInput = input("Shall we continue the program once more")
    userInput = userInput.lower()

print("END PROGRAM")

