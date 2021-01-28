#loops with else

#only something in python

countdown = 10

while (countdown > 0):
    print(countdown,"!")
    countdown = countdown -1
#acts as a way to do something after the loop naturally ends
else:
    print("Blastoff")

print("--------------------------------------------------")
print()

for x in range(1,11):

    #checks remainder when dividing by 2, 0 means even
    if x % 2 == 0:
        print("there is an even number in the list")
        break
#else is here for list being odd
else:
    print("these numbers were all odd")

for x in range(1,11,2):

    #checks remainder when dividing by 2, 0 means even
    if x % 2 == 0:
        print("there is an even number in the list")
        break
#else is here for list being odd
else:
    print("these numbers were all odd")
