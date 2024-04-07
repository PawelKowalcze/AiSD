from math import *


class Circle:
    r = int(input('Insert radius of a circle'))
    func_stop = False

    if r < 0:
        func_stop = True

    def area(self):
        if not self.func_stop:
            return pi * (self.r * self.r)
        else:
            print('Circle cant be created')
            pass

    def perimeter(self):
        if not self.func_stop:
            return 2 * pi * self.r
        else:
            print('Circle cant be created')
            pass


class Triangle:
    func_stop = False
    a = int(input('Insert first diameter of a triangle'))
    b = int(input('Insert second diameter of a triangle'))
    c = int(input('Insert third diameter of a triangle'))
    diameters = [a, b, c]
    diameters.sort()
    # print(diameters[2])
    sin_alpha = 0
    if diameters[2] < (diameters[0] + diameters[1]) and all(diameter > 0 for diameter in diameters):
        # a**2 = b**2 + c**2 -2*b*c*cos(alfa)
        # cos(alfa) = (a**2 - b**2 - c**2)/(-2*b*c)
        cos_alfa = (a ** 2 - b ** 2 - c ** 2) / (-2 * b * c)
        # print(cos_alfa)
        sin_alpha = sqrt(1 - cos_alfa ** 2)
        # print(sin_alpha)
    else:
        func_stop = True

    def area(self):
        if not self.func_stop:
            # print(self.func_stop)
            return round(self.b * self.c * self.sin_alpha / 2, 2)
        else:
            print('The triangle cant be created')
            pass

    def perimeter(self):
        if not self.func_stop:
            return self.a + self.b + self.c
        else:
            print('The triangle cant be created')
            pass


class Square:
    func_stop = False
    a = int(input('Insert diameter of side of a square'))
    if a < 0:
        func_stop = True

    def area(self):
        if not self.func_stop:
            return self.a ** 2
        else:
            print('Square cant be created')
            pass

    def perimeter(self):
        if not self.func_stop:
            return 4 * self.a
        else:
            print('Square cant be created')
            pass

# obj1 = Circle()
# print('Area: ' + str(obj1.area()))
# print('Perimeter: ' + str(obj1.perimeter()))
# obj2 = Triangle()
# print('Area: ' + str(obj2.area()))
# print('Perimeter: ' + str(obj2.perimeter()))
# obj3 = Square()
# print('Area: ' + str(obj3.area()))
# print('Perimeter: ' + str(obj3.perimeter()))
