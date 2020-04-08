amountofchange = input('Enter the amount of change needed in cents: ')
amountofchange = int(amountofchange)

print ('Give ' + str(amountofchange // 200) + ' toonie(s) of change')
amountofchange = amountofchange % 200

print ('Give ' + str(amountofchange // 100) + ' loonie(s) of change')
amountofchange = amountofchange % 100

print ('Give ' + str(amountofchange // 25) + ' quarter(s) of change')
amountofchange = amountofchange % 25

print ('Give ' + str(amountofchange // 10) + ' dime(s) of change')
amountofchange = amountofchange % 10

print ('Give ' + str(amountofchange // 5) + ' nickel(s) of change')
amountofchange = amountofchange % 5

print ('Give ' + str(amountofchange // 1) + ' pennies of change')
amountofchange = amountofchange % 1