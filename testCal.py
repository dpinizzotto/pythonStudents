start = int(input("Start day"))

days = int(input("days in the month"))

counter=0

for x in range(1, days+1):
    
    counter = counter +1

    while(start > 1):
        print("", end="\t")
        start=start-1
        
        counter = counter +1
    else:
        print(x,end="\t")
        
    if counter % 7 == 0:
        print()
        
