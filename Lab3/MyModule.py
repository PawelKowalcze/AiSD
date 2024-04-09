from math import *


class Circle:
    func_stop = False

    def __init__(self, r):
        self.radius = r
        self.func_stop = r < 0

    def area(self):
        if not self.func_stop:
            return pi * (self.radius * self.radius)
        else:
            print('Circle cant be created')

    def perimeter(self):
        if not self.func_stop:
            return 2 * pi * self.radius
        else:
            print('Circle cant be created')


class Triangle:
    func_stop = False

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        self.diameters = [a, b, c]
        self.diameters.sort()
        print(self.diameters)
        self.sin_alpha = 0
        if self.diameters[2] < (self.diameters[0] + self.diameters[1]) and all(diameter > 0 for diameter in self.diameters):
            cos_alfa = (a ** 2 - b ** 2 - c ** 2) / (-2 * b * c)
            # print(cos_alfa)
            self.sin_alpha = sqrt(1 - cos_alfa ** 2)
            # print(sin_alpha)
        else:
            self.func_stop = True

    def area(self):
        if not self.func_stop:
            # print(self.func_stop)
            return round(self.b * self.c * self.sin_alpha / 2, 2)
        else:
            print('The triangle cant be created')

    def perimeter(self):
        if not self.func_stop:
            return self.a + self.b + self.c
        else:
            print('The triangle cant be created')


class Square:
    func_stop = False

    def __init__(self, a):
        self.a = a

        if self.a < 0:
            self.func_stop = True

    def area(self):
        if not self.func_stop:
            return self.a ** 2
        else:
            print('Square cant be created')

    def perimeter(self):
        if not self.func_stop:
            return 4 * self.a
        else:
            print('Square cant be created')

#x = int(input('Enter a number: '))
#obj1 = Circle(x)
#print(obj1.area())
#print(obj1.perimeter())
#print('Area: ' + str(obj1.area()))
#print('Perimeter: ' + str(obj1.perimeter()))
#y = int(input('Enter a number: '))
#x = int(input('Enter a number: '))
#z = int(input('Enter a number: '))
#obj2 = Triangle(x, y, z)
#print('Area: ' + str(obj2.area()))
#print('Perimeter: ' + str(obj2.perimeter()))
#obj3 = Square(x)
#print('Area: ' + str(obj3.area()))
#print('Perimeter: ' + str(obj3.perimeter()))
