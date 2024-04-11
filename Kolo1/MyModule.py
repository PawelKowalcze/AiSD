class LICZBA:
    number = 0

    def __init__(self, value):
        if type(value) == int:
            self.number = value
        else:
            print('Value is not an integer')


class WYRAZ:
    characters = ''
    def __init__(self, characters):
        if type(characters) == str:
            self.characters = characters
        else:
            print('Characters is not a string')


def DODAJ(object1, object2):
    if type(object1) == LICZBA and type(object2) == LICZBA:
        return object1.number + object2.number
    if type(object1) == WYRAZ and type(object2) == WYRAZ:
        return object1.characters + object2.characters
    else:
        return object1.number + ord(object2.characters[-1])


def ODEJMIJ(object1, object2):
    if type(object1) == LICZBA and type(object2) == LICZBA:
        return object1.number - object2.number
    if type(object1) == WYRAZ and type(object2) == WYRAZ:
        if len(object1.characters) > len(object2.characters):
            return object1.characters
        else:
            return object2.characters
    else:
        print('???')

'''
x = int(input('Enter a number: '))
Number = LICZBA(x)
print(Number.number)

y = input('Enter a word: ')
word = WYRAZ(y)
print(ord(word.characters[-1]))

print(DODAJ(Number, word))
print(DODAJ(Number, Number))
print(DODAJ(word, word))

print(ODEJMIJ(Number, word))
print(ODEJMIJ(Number, Number))
print(ODEJMIJ(word, word))
'''

if __name__ == "__main__":
    print(DODAJ(LICZBA(5), LICZBA(10)))
    print(DODAJ(WYRAZ("QWERTYT"), WYRAZ("DDDDDDFASDFS")))
    print(DODAJ(LICZBA(5), WYRAZ("DDDDDDFASDFS")))

    print(ODEJMIJ(LICZBA(5), LICZBA(10)))
    print(ODEJMIJ(WYRAZ("QWERTYT"), WYRAZ("DDDDDDFASDFS")))
    print(ODEJMIJ(LICZBA(5), WYRAZ("DDDDDDFASDFS")))
