from random import *
'''

class LOTTO:
    l = []

    def __init__(self, l):
        self.l = l
        self.l.sort()
        # print(self.l)

    def ret(self):
        return self.l


def SPRAWDZ(o1, o2):
    print(o1)
    print(o2)
    if o1 == o2:
        return True
    else:
        return False

def GRAJ(n,isequal):
    attempts = n
    if isequal:
        print('Values are the same')



for i in range(0, 6):
    l.append(randint(0, 48))



n = int(input("How many attempts?"))
Obj1 = LOTTO(l)
Obj2 = LOTTO(l)


print(SPRAWDZ(Obj1.ret(), Obj2.ret()))
'''

f = open(f'Name', 'w')
f.writelines(f"XDD")
f.close()