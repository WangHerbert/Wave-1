sec = input('Enter the total number of seconds: ')
seconds = int(sec)

days = (seconds // 86400)
seconds = (seconds % 86400)

hours = (seconds // 3600)
seconds = (seconds % 3600)

minutes = (seconds // 60)
seconds = (seconds % 60)

print (str(sec) + ' seconds is equal to %d:%02d:%02d:%02d' % (days, hours, minutes, seconds))