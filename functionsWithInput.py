#functions with input
import math
#main method for everything to run
def main():
    #get user input
    userLength = float(input("Enter the length: "))
    userWidth = float(input("Enter the width: "))
    #call method
    rectangleArea(userLength, userWidth)

    #get the side lengths
    a,b = [float(x) for x in input("enter the side lengths: ").split()]

    #call the method with given values
    pythagoreanTheorem(a,b)




#other methods
    
#methods with input have things in the brackets
def rectangleArea(length, width):
    if length <0 or width< 0:
        print("Error, cannot calculate with negative values")
    else:
        #just do the math
        area = length*width
        print("The area is",area)

#this is like your formula name and the givens go in the bracket
def pythagoreanTheorem(a,b):
    #we go through our steps but with variables, not numbers
    #it's really like writing our formula
    c = math.sqrt((a**2+b**2))

    #right now we are always printing the result
    print("the value of c is",c)
    


#most important
main()
