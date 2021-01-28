#read and write to files

#june 1, 2020

def main():
    print("""Welcome to the program.
Press 1 to write to a file
Press 2 to read the current file
Press 3 to quit""")
    userChoice = int(input("Enter choice: "))
    while userChoice < 1 or userChoice >3:
        print()
        print("Error, choose again.")
        userChoice = int(input("Enter choice: "))

    if userChoice == 1:
        writeToFile()
    elif userChoice ==2:
        readFromFile()
    else:
        exit()



def writeToFile():
    #first thing we are going to do is open the file ***
    #in the open method, w=write, a = append
    savedFile = open('names.txt','a')

    runAgain = input("Do you have names to save to a file? ").lower()
    while runAgain == "yes":
        name = input("Enter a name to save: ")

        #to save it
        savedFile.write(name+"\n")

        #keep the loop user prompted
        runAgain = input("Do you more have names to save to a file? ").lower()

    else:
        print("Ok, done for now, saving file")
        #to save the file
        savedFile.close()


def readFromFile():
    #first thing we are going to do is open the file ***
    #in the open method, r=read
    savedFile = open('names.txt','r')

    line = savedFile.readline()

    while line != '':
        print(line,end="")
        line = savedFile.readline()

    #to save the file
    savedFile.close()
    



main()




        
