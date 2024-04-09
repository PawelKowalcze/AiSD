from MyModule import *

x = int(input('Enter a number: '))
circle = Circle(x)
print(circle.area())
x = int(input('Enter a number: '))
y = int(input('Enter a number: '))
z = int(input('Enter a number: '))
Triangle = Triangle(x, y, z)
print('Area: ' + str(Triangle.area()))
print('Perimeter: ' + str(Triangle.perimeter()))

