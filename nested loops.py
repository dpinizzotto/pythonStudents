#For and while loop review/nested loops
#Mr Pinizzotto
#April 6

#while loops need a condition to run
#ask for user input to run the program
#going to force it to be lower case
runAgain = input("Do you want to run the program to print some multiplication? ").lower()
print()

while(runAgain == "yes" or runAgain == "y"):

    #get the number that they want to find the multipcation for
    multiplication = int(input("What number do you want to see multiplication for? "))
    print()
    #how far they want to go
    end = int(input("Where would you like to end? "))
    print()

    for x in range(1,end+1):
        print(multiplication,"x", x, "=", (multiplication*x))



    print()
    #ask the question again
    runAgain = input("Do you want to run the program again to print some new multiplication? ").lower()

#leaves the loop (ie. say no)
print("Ok Bye!")
