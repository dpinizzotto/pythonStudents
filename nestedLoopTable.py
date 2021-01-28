

rows = int(input("How many rows: "))
columns = int(input("How many columns: "))
skip = input("Do you want to count by 2's? ").lower()

if skip == "yes":
    for x in range(1,rows+1,2):
        
        for y in range(1,columns+1,2):
            
            #this will print the cell coordinate
            print(f"({x},{y})", end="\t")

        #this will print a newline at the end of the row
        print("")
else:
    for x in range(1,rows+1):
        
        for y in range(1,columns+1):
            
            #this will print the cell coordinate
            print(f"({x},{y})", end="\t")

        #this will print a newline at the end of the row
        print("")
