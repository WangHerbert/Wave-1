import math

radius = (input('Enter the radius of the cylinder: '))
height = (input('Enter the height of the cylinder: '))

radius = float(radius)
height = float(radius)

volume = (radius ** 2 * math.pi) * height
volume = round(volume, 1)

print ('The volume of the cylinder is ' + str(volume) + ' units squared')