class Class1:
    a = '123'

    def __init__(self, b):
        self.a = b

    def print1(self):
        a = '321'
        print(a)
        print(self.a)


obj1 = Class1('5')
obj1.print1()
print(obj1.a)
