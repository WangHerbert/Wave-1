import math

radius = float(input('Enter the radius of the cylinder: '))
height = float(input('Enter the height of the cylinder: '))

volume = (radius ** 2 * math.pi) * height

print ('The volume of the cylinder is ' + str(round(volume,1)) + ' units squared')