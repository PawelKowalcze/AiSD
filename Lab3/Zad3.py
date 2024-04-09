from math import *
from random import *


class MonteCarlo:

    def __init__(self, x1, x2, attempts):
        self.ratio = 0
        self.attempts = attempts
        self.counttrue = 0
        self.x1 = x1
        self.x2 = x2
        self.y1 = 0
        self.y2 = 1

    def Random(self):
        for i in range(1, self.attempts):
            x = uniform(self.x1, self.x2)
            #print(x)
            y = uniform(self.y1, self.y2)
            #print(y)
            print(sin(x))
            if  sin(x) >= y:
                self.counttrue += 1
        self.ratio = self.counttrue / self.attempts
        print(self.ratio)
        return self.ratio * abs(self.x1 - self.x2) + abs(self.y1 - self.y2)


attempts = int(input("How many attempts do you want to use?"))
bound1 = int(input("Insert first boundary of integration :"))
bound2 = int(input("Insert second boundary of integration :"))
Object = MonteCarlo(bound1, bound2, attempts)
print(Object.Random())
