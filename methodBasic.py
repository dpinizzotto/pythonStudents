#basic methods

# new format, always have a main method to run the code
#this is very traditional for all languages
#all the methods will be called here
def main():
    print("""Select from the following
1.Message
2.Math

""")
    choice= int(input("Enter your selection here: "))
    if choice ==1:
        getUserInput()
    elif choice ==2:
        getArea()
    else:
        print("Error, not valid")



#all other methods go below to define (they will not run)
def getUserInput():
    firstName = input("enter your name: ")
    age = int(input("enter your age: "))
    print("Hello",firstName)
    


def getArea():
    length = int(input("Enter length: "))
    width = int(input("Enter length: "))
    print("Area is",(length*width))


#this one line will make everything work
main()
