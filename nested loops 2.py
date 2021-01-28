#nested loops again
#mr pinizzotto
#april 8

#we can actually do for loop in a for loop

#say we wanted to print 10-20 times tables
for x in range(10,21):
    for y in range (10,21):
        #the end= forces it to not go to a new line
        print(x*y,end="\t")
        
    #this will make a new line after 1-10
    print()

