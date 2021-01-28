# Merit or honours calculator
# Description: Making a program that will determine if we get merit or honours, or nothing
# Mr Pinizzotto
# Dec 1, 2020

# get the student's name
name = input("What is your name? ")

# get 4 grades from the user
grade1 = int(input("What is your first grade? "))
grade2 = int(input("What is your second grade? "))
grade3 = int(input("What is your third grade? "))
grade4 = int(input("What is your fourth grade? "))


#calculate the average
averageGrade = (grade1+grade2+grade3+grade4)/4

#determine whether merit or honours was earned
#merit range
if averageGrade >= 74.5 and averageGrade < 79.5:
    #print the response
    print(f"Your average is {averageGrade:.2f}\nGreat work. A merit award is meritted")

#honours range
elif averageGrade >= 79.5 and averageGrade <= 100:
    #print the response
    print(f"Your average is {averageGrade:.2f}\nAmazing! It is an honour to give you to honours.")

#check over 100
elif averageGrade > 100:
    print(f"Your average is {averageGrade:.2f}\nMaybe check the math, this shouldn't happen")

#this is for everything other than 74.5 and up
else:
    #response
    print(f"Your average is {averageGrade:.2f}\nDISAPPOINTED!")

#better:
#if average > 100
#elif average >= 79.5
#elif average >= 74.5
#else
        
