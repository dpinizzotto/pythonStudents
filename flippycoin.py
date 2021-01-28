#turn taking with two players
#mr pinizzotto
#april 21

from random import *

player1Total = 0
player2Total = 0

#this will make my game run
while True:
    #ask plyer 1 to go
    player1Go = input("P1, flip the coin? ").lower()

    #player 1 turn
    while player1Go == "yes" or player1Go == "y":

        #generate the flip (1 is heads 2 is tails)
        flip = randint(1,2)

        #ask the user to make a guess
        p1Guess = input("Heads or tails? ").lower()

        print("Flipping.....")

        if flip == 1 and p1Guess == "heads":
            print("P1 gets the point!!")
            #add to the total score
            player1Total +=1

        elif flip == 2 and p1Guess == "tails":
            print("P1 gets the point!!")
            #add to the total score
            player1Total +=1
        elif flip == 1 and p1Guess == "tails":
            print("P2 gets the point!!")
            #add to the total score
            player2Total +=1
        else:
            print("P2 gets the point!!")
            #add to the total score
            player2Total +=1

        #ask if the player wants to go again
        player1Go = input("P1, flip the coin again? ").lower()
    

    if player1Go == "no" or player1Go == "n":
        break

#if they say no the loop ends and we have to figure out a winner
if player1Total > player2Total:
    print("P1 wins!!")
elif player2Total > player1Total:
    print("Player 2 wins")
else:
    print(" we have a draw")




