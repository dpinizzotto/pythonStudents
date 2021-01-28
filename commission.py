keep_going = 'y'
while keep_going == 'y':
    #get salespersons sales and commission rate
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

    #calculate the commission
    commission = sales * comm_rate

    #display the commission.
    print('The comission is $',format(commission,'.2f'))

    #see if the user wants another one
    keep_going = input('Do you want to do another calculation (y or n)')

#print an end message for the user
print('End Program')
