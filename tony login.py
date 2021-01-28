#Anthony Wilson
#Decision Structures Summative
#Login / Register System
#27/03/18

#Imports
#Used for read and write to store logins
import pickle
#Used to get system paths
import os
#Path object
from pathlib import Path

#Default list of usernames and passcodes for writing if the login file doesn't exist already
logins = {'Bowser4Life': '1234'}
#(This will also hold the existing logins loaded from file as it would be inefficiant to load the file and read through it everytime someone wants to login.

#Location for saving login data
loginPathStr = os.getcwd() + '/logins.pkl'
#I'm using a path based on where the program is ran from for compatibility while moving from OS's

#Path object from string
loginPath = Path(loginPathStr)

#Admin password for listing passcodes
adminPass = "admin8"

#Added bool for debugging
debug = True

#Print login path for debug
print(loginPathStr)

#Methods for saving and loading logins to the file and hashmap
def saveLogins():
    #Open file for writing and gives is the variable f
    with open(loginPathStr, 'wb') as f:
        #Dumps data from the logins hashmap to the file 'f' using the pickle class and the highest protocal saves it as a binary format (since python 2.3) *could change as it will always use the highest
        pickle.dump(logins, f, pickle.HIGHEST_PROTOCOL)
def loadLogins():
    with open (loginPathStr, 'rb') as f:
        itemlist = pickle.load(f)
        
#Returns if the login file exists already
def loginsExists():
    if loginPath.exists():
        return True
    else:
        return False

#If login file exists read with pickle and set logins from the hashmap saved to file
if loginsExists() == True:
    loadLogins()
#If login file does not exist with pickle write the default set defined (logins)
else:
    saveLogins()

#Variable for the loop to login and register
running = True

#Tell user the interface
def listInterface():
    print("PLEASE NOTE: Passcodes must be 4 digits.")
    print()
    print("Please enter a following command...")
    print("login (username) (passcode) | Logs into existing account.")
    print("register (username) (passcode) | Registers new account.")
    print("delete (username) (passcode) | Deletes account from system.")
    print("list [admin passcode]| List user accounts. | admin mode lists passcodes associated.")
    print("exit")
    print()

#List accounts
def listAccounts(withPass):
    #Loop for every user(key) in logins
    for user in logins:
        #Prints username
        print("Username: " + user)
        #Checks if admin mode is on
        if withPass == True:
            #Prints passcode for account
            print("Passcode: " + logins[user])
            #Print line for space
        print()

#Login method
def login(username, passcode):
    #Checks if username is already registered
    if username not in logins:
        #Returning the problem
        return "User doesn't exist."
    #Checks if passcode matches the passcode on file
    if passcode != logins[username]:
        #Returns a problem
        return "Passcode is incorrect!"
    #Returns true if worked
    return "True"
    #(Will return the error if one came across)


#Register method
def register(username, passcode):
    #Checks if username is already registered
    if username in logins:
        #Returning the problem
        return "Username already exists."
    #Checks if passcode is anything except 4 charactors
    if len(passcode) != 4:
        return "Passcode must be 4 digits."
    #Trys to change passcode string to an int
    passcodeInt = 0
    try:
        passcodeInt = int(passcode)
    except ValueError:
        return "The passcode must be a number."
    #Adds login to hashmap
    logins[username] = passcode
    #Returns true if worked
    return "True"
    #(Will return the error if one came across)


#Delete account method
def delete(username, passcode):
    #Checks if username is already registered
    if username not in logins:
        #Returning the problem
        return "User does not exist"
    #Checks if passcode matches the passcode on file
    if passcode != logins[username]:
        #Returns a problem
        return "Passcode is incorrect!"
    #Removes login from hashmap
    del logins[username]
    #Returns true if worked
    return "True"
    #(Will return the error if one came across)


#Loop commands
while(running):
    listInterface()
    #Input split into a list
    cmd = input("Please enter a command: ").split()
    #Make sure input has a command
    if len(cmd) > 0:
        #Check the first string in the list
        if cmd[0] == "login":
            #If they give a command and 2 args
            if len(cmd) == 3:
                result = login(cmd[1], cmd[2])
                if result == "True":
                    print("Successfully logged in!")
                    break
                else:
                    print(result)
            else:
                print("Must have 2 variables after 'register'.")
        elif cmd[0] == "register":
            #If they give a command and 2 args
            if len(cmd) == 3:
                result = register(cmd[1], cmd[2])
                if result == "True":
                    print("Successfully registered!")
                else:
                    print(result)
            else:
                print("Must have 2 variables after 'register'.")
        elif cmd[0] == "delete":
            #If they give a command and 2 args
            if len(cmd) == 3:
                result = delete(cmd[1], cmd[2])
                if result == "True":
                    print("Successfully deleted account!")
                    break
                else:
                    print(result)
            else:
                print("Must have 2 variables after 'register'.")
        elif cmd[0] == "list":
            #Checks if the user submitted 1 cmd and 1 arg and the arg was the preset admin passcode
            if len(cmd) == 2 and cmd[1] == adminPass:
                #Lists accounts with passcode
                listAccounts(True)
            else:
                #Lists accounts without passcode
                listAccounts(False)
        elif cmd[0] == "exit":
            quit()




