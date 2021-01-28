#for loops
from random import randint
#basic loop
##print("Range(5)")
##for i in range(5):
##    print(i)
##else:
##    print("end")
##
##print("Range(7,12)")
##for i in range(7,12):
##    print(i)
##else:
##    print("end")
##
##
##print("Range(1,20,4)")
##for i in range(1,20,4):
##    print(i)
##else:
##    print("end")

#go by user input
stopAmount = int(input("How many die rolls do you want? "))
for x in range(1,stopAmount+1):
    roll1 = randint(1,6)
    roll2 = randint(1,6)
    print(f"Die roll {x}:{roll1} and {roll2}")

    if roll1 == roll2:
        print("doubles!")
        if(roll1 == 1):
            print("Snake eyes")
            break
        else:
            break
else:
    print("no doubles rolled")
