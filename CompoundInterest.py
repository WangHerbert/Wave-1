savings = float(input('Enter the amount of money deposited into the savings account: '))

interestyear1 = 1.04
interestyear2 = 1.04 ** 2
interestyear3 = 1.04 ** 3

year1total = round (savings * interestyear1, 2)
year2total = round (savings * interestyear2, 2)
year3total = round (savings * interestyear3, 2)

print ('The money in the savings account after 1 year is $' + str(year1total))
print ('The money in the savings account after 2 years is $' + str(year2total))
print ('The money in the savings account after 3 years is $' + str(year3total))