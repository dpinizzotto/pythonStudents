#add if statements for the different things people type in

age = int(input("Please enter your age: "))

if(age>=0 and age <12):
    print("You are still a kid")
    print()
elif(age >= 12 and age <=19):
    print("You are a teenager")
    print()
elif(age >=20 and age <35):
    print("You are a young adult")
    print()
elif(age >=35 and age <65):
    print("You are an adult")
    print()
else:
    print("You are old")
    print()


hoursWorked = float(input("Enter your hours worked this week: "))

if hoursWorked <= 40:
    print("You did not work overtime!")
else:
    print("you worked overtime!")


day = input("what is your favourite day of the week? ").lower()

if day == "monday":
    print("are you mad!!!!")
