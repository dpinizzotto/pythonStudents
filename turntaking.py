#Making a two player game
#Mr Pinizzotto
#April 21

from random import *

player1Total = 0
player2Total = 0

##while player1Total < 20 or player2Total <20:
while True:
    player1Go = input("Would p1 like to guess the flip").lower()

    while player1Go=="yes" or player1Go == "y":
        p1Guess = input("Guess heads or tails").lower()
    #assume 1 is heads and 2 is tails
        flip = randint(1,2)
        
        if flip == 1 and p1Guess == "heads":
            print("P1 gets the point")
            #this adds one to the player total
            player1Total = player1Total + 1

        elif flip == 1 and p1Guess == "tails":
            print("P2 gets the point")
            player2Total = player2Total + 1

        elif flip == 2 and p1Guess == "tails":
            print("P1 gets the point")
            player1Total = player1Total + 1

        else:
            print("P2 gets the point")
            player2Total = player2Total + 1
            
        print("Flipping....")
        player1Go = input("Would p1 like to guess the flip").lower()
        
            

    player2Go = input("Would p2 like to guess the flip").lower()
    while player2Go=="yes" or player2Go =="y":
        print("Flipping....")
        player2Go = input("Would p2 like to guess the flip").lower()

    if player2Go=="no" or player2Go =="n" or player1Go=="no" or player1Go =="n":
        break

#if they say no the loop ends and we have to figure out a winner
if player1Total > player2Total:
    print(name, " wins!!")
elif player2Total > player1Total:
    print("Player 2 wins")
else:
    print(" we have a draw")
