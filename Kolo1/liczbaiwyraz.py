#MyModule
class LICZBA:
    a = 0
    def __init__(self,a):
        self.a = a

    def DODAJ(self, other):
        if type(other) == LICZBA:
            return self.a + other.a
        elif type(other) == WYRAZ:
            return ord(other.b[-1]) + self.a

    def ODEJMIJ(self, other):
        if type(other) == LICZBA:
            return self.a - other.a
        elif type(other) == WYRAZ:
            z = "???"
            return z

    def ZAPISZ(self, other):
        dane = open("wyniki.txt", 'a')

        if type(other) == LICZBA:
            dane.writelines(str(self.DODAJ(other)) + '\n')  # LICZBA + LICZBA
            dane.writelines(str(self.ODEJMIJ(other)) + '\n') # LICZBA - LICZBA

        elif type(other) == WYRAZ:
            dane.writelines(str(self.DODAJ(other)) + '\n') #LICZBA + WYRAZ
            dane.writelines(str(self.ODEJMIJ(other)) + '\n') #LICZBA - WYRAZ

        dane.close()

class WYRAZ:
    b = ''
    def __init__(self, b):
        self.b = b

    def DODAJ(self, other):
        if type(other) == WYRAZ:
            return self.b + other.b
        elif type(other) == LICZBA:
            return ord(self.b[-1]) + other.a

    def ODEJMIJ(self, other):
        if type(other) == WYRAZ:
            if len(other.b) > len(self.b):
                return len(other.b)
            else:
                return len(self.b)
        elif type(other) == LICZBA:
            return "???"

    def ZAPISZ(self, other):
         dane = open("wyniki.txt", 'a')

         if type(other) == LICZBA:
            dane.writelines(str(self.DODAJ(other)) + '\n')  # WYRAZ + LICZBA
            dane.write(str(self.ODEJMIJ(other)) + '\n')  # WYRAZ - LICZBA
         elif type(other) == WYRAZ:
            dane.writelines(str(self.DODAJ(other))+ '\n')  # WYRAZ + WYRAZ
            dane.writelines(str(self.ODEJMIJ(other)) + '\n')  # WYRAZ - WYRAZ

         dane.close()


if __name__ == "__main__":
    l1 = LICZBA(5)
    l2 = LICZBA(3)

    w1 = WYRAZ("kocham")
    w2 = WYRAZ("pythona")

    #TESTOWANIE WENĄTRZ KLASY
    print("DZIAŁANIE METOD DODAJ(): ")
    print("LICZBA + LICZBA: ", l1.DODAJ(l2))
    print("LICZBA + WYRAZ: ", l1.DODAJ(w1))
    print("WYRAZ + WYRAZ: ", w1.DODAJ(w2))
    print("WYRAZ + LICZBA: ", w1.DODAJ(l1))

    print("DZIAŁANIE METOD ODEJMIJ(): ")
    print("LICZBA - LICZBA: ", l1.ODEJMIJ(l2))
    print("LICZBA - WYRAZ: ", l1.ODEJMIJ(w1))
    print("WYRAZ - LICZBA: ", w1.ODEJMIJ(l1))
    print("WYRAZ - WYRAZ: ", w1.ODEJMIJ(w2))

    #TESTOWANIE ZAPISU

    l1.ZAPISZ(l2)
    l1.ZAPISZ(w1)
    w1.ZAPISZ(l1)
    w1.ZAPISZ(w2)
