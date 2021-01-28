import time

#Menu items
# format: "Name",Price,QTY
HB = ["Hamburger", 1.99,0]
CM = ["Chocolate milk",0.99,0]
CT = ["Chicken Tenders",4.99,0]
FS = ["Fries",1.49,0]
CK = ["Cake",0.99,0]


#naming what you ordered
name = input("enter your name:")
time.sleep(1.0)
print()
print("Hey",name)
time.sleep(1.0)
print()
print("you want to order:")
print()

#print menu
print('%15s' % "MENU")
print('%15s' % HB[0],'%5s' % HB[1])
print('%15s' % CM[0],'%5s' % CM[1])
print('%15s' % CT[0],'%5s' % CT[1])
print('%15s' % FS[0],'%5s' % FS[1])
print('%15s' % CK[0],'%5s' % CK[1])


#food variables
HB[2] = float(input("Enter how many " + HB[0] + "s:"))
CM[2] = float(input("Enter how many " + CM[0] + "s:"))
CT[2] = float(input("Enter how many " + CT[0] + ":"))
FS[2] = float(input("Enter how many " + FS[0] + ":"))
CK[2] = float(input("Enter how many " + CK[0] + "s:"))


#recipt w/o tax and tip
#subtotal = (Chicken tenders+Fries+Chocolate milk+cake)
subtotal = HB[2]*HB[1] + CM[2]*CM[1] + CT[2]*CT[1] + FS[2]*FS[1] + CK[2]*CK[1] 


print("your subtotal is $"+str(format(subtotal, '.2f')))
time.sleep(1.0)
print()

#your recipt accounting for sales tax
Harmonized_tax = float(subtotal*0.13)
Order_Total = Harmonized_tax + subtotal
print("Sales tax is $"+str(format(Harmonized_tax, '.2f')))
print("with sales tax, you total is $"+str(format(Order_Total, '.2f')))
time.sleep(1.0)
print()

#recipt with tip option
tip_percent = float(input("Enter how much you would like to tip (%):  "))/100
tip_amount = subtotal*tip_percent # Dont tip the tax
total__with_tip = float((Order_Total+tip_amount))


print()
print(name,"your tip was $"+str(format(tip_amount, '.2f')))
time.sleep(1.0)
print()
print(name,"your total is $"+str(format(total__with_tip, '.2f')))
