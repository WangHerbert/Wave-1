days = int(input('Enter number of days: '))
hours = int(input('Enter number of hours: '))
minutes = int(input('Enter number of minutes: '))
seconds = int(input('Enter number of seconds: '))

hours = hours + (days * 24)
minutes = minutes + (hours * 60)
seconds = seconds + (minutes * 60)

print ('The total number of seconds is %s ' %(seconds))