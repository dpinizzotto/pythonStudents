#functions with return statements
firstName=""
lastName=""
#main to run all the code
def main():
    #catch and call a method that returns
    #firstName,lastName =
    getInfo()

    print(f"Hello {firstName} {lastName}")

    age = getAge()
    print(f"You are {age} today and will be {age+10} next decade")




#other methods
def getInfo():
    global firstName,lastName
    firstName,lastName= input("Enter your name: ").split()

    #return fName,lName


def getAge():
    age = int(input("Enter your age: "))

    return age


main()
