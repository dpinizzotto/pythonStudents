check = input("Do you want to calculate the pay of an employee?")

while check == "yes" or check == "Yes":
    name = input("What is the employee's name?")
    try:
        hoursWorked = float(input("How many hours did they work?"))
    except ValueError:
        print("ERROR: please enter a valid number")
        continue
    else:
        break

    try:
        payRate = float(input("What is their hourly pay?"))
    except ValueError:
        print("ERROR: please enter a valid number")
        continue
    else:
        break

    totalPay = hoursWorked * payRate

    print(name,"'s total pay is $", format(totalPay,".2f"))
    check = input("Do you want to calculate the pay of an employee?")

print("END OF PROGRAM")
    
