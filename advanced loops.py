#Grade Average calculator
#Mr Pinizzotto
#April 8

#always set up a variable outside the loop
total = 0

#ask how many grades we are adding
maxGrades = int(input("How many grades are we adding together? "))
print()

#input validation
while maxGrades < 2:
    #print error message
    print("Error, must have more than 1 grade to work")
    maxGrades = int(input("How many grades are we adding together? "))
    print()

#now we will get the grades for each one
for x in range(maxGrades):

    grade = int(input("Please enter the grade: "))
    print()
    
    #validate input
    while grade < 0:
        print("Error, must be over 0")
        grade = int(input("Please enter the grade: "))
        print()

    #when the grade is correct, add it to the total
    total = total + grade

#we will do the average
average = total/maxGrades

print("your average is",average)

