#While loop basics

#we set up a counter for how many grades were entered
counter = 0

#a running total
total=0

#heres my if condition to run the code
runAgain = input("Do you want to calculate your average? ").lower()

while(runAgain == "yes"):
    counter+=1

    grade = int(input("Enter your grade: "))

    total+=grade

    #***Super Important***#
    #we need to ask the question again
    runAgain = input("Do you have more grades to enter? ").lower()

    #error handling (More advanced)
    while runAgain != "no" and runAgain != "yes":
        print("Error, not correct information, try again")
        runAgain = input("Do you have more grades to enter? ").lower()


else:
    average = total/counter
    print(f"Your average is {average:.2f}")
