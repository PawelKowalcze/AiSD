class LICZBA:
    value = 0

    def __init__(self, value):
        if type(value) == int:
            self.value = value
        else:
            print("value must be an integer!")
            exit()


class WYRAZ:
    value = ""

    def __init__(self, value):
        if type(value) == str:
            self.value = value
        else:
            print("value must be a string!")
            exit()

# mozliwe ze zle zinterpretowalem polecenie - dlatego mam funkcje poza klasami
# trzeba sie spytac jak bedzie cos podobnego


def DODAJ(first_class, second_class):
    if type(first_class) not in (LICZBA, WYRAZ) or type(second_class) not in (LICZBA, WYRAZ):
        print("WRONG TYPE")
        exit()
    else:
        if type(first_class) == type(second_class):
            return first_class.value + second_class.value
        else:
            if type(first_class) == WYRAZ:
                return ord(first_class.value[-1]) + second_class.value

            elif type(second_class) == WYRAZ:
                return ord(second_class.value[-1]) + first_class.value


def ODEJMIJ(first_class, second_class):
    if type(first_class) not in (LICZBA, WYRAZ) or type(second_class) not in (LICZBA, WYRAZ):
        print("WRONG TYPE")
        exit()
    else:
        if type(first_class) == type(second_class) == LICZBA:
            return first_class.value - second_class.value
        elif type(first_class) == type(second_class) == WYRAZ:
            if len(first_class.value) > len(second_class.value):
                return first_class.value
            elif len(first_class.value) < len(second_class.value):
                return second_class.value
        else:
            return "???"


if __name__ == "__main__":
    print(DODAJ(LICZBA(3), LICZBA(4)))
    print(DODAJ(WYRAZ("QWERTY"), WYRAZ("UIOP")))
    print(DODAJ(LICZBA(69), WYRAZ("TESTOWANIE")))

    print(ODEJMIJ(LICZBA(188), LICZBA(88)))
    print(ODEJMIJ(WYRAZ("DLUZSZY"), WYRAZ("KROTSZY??????")))
    print(ODEJMIJ(WYRAZ("TRZY"), WYRAZ("DWA")))
    print(ODEJMIJ(WYRAZ("CO SIE STANIE"), LICZBA(1024)))



