#Getting input from user and making some code/programs do math

#to get input we need to set up a variable
name = input("What is your name? ")

print("hello, "+name+"!\n")

#plain numbers (whole numbers) are ints
age = int(input("What is your age? "))

print("woah thats old!!")

#calculate the BMI
#floats are decimals
weight = float(input("Enter your weight in lbs: "))
height = float(input("Enter your height in inches: "))

#we can type the formula and python will do it
BMI = (weight/(height ** 2))*703

#this line prints the answer without formating (lots of decimal places)
print(BMI)

#this prints it fancy
print(f"Your BMI is {BMI:.2f}. That's ok for a {age} year old")
