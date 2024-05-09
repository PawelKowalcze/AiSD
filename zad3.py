import math
import numpy as np
import random

class Wezel:
    def __init__(self, wartosc):
        self.wartosc = wartosc
        self.lewy = None
        self.prawy = None

    def INSERT(self, dane):
        if self.wartosc is None:
            self.wartosc = dane
            return
        elif self.wartosc == dane:
            return
        else:
            if dane < self.wartosc:
                if self.lewy is None:
                    self.lewy = Wezel(dane)
                else:
                    self.lewy.INSERT(dane)
            elif self.wartosc < dane:
                if self.prawy is None:
                    self.prawy = Wezel(dane)
                else:
                    self.prawy.INSERT(dane)

    def WYSWIETL(self, level=0, is_right=False):
        if is_right:
            print(' ' * 4, (level - 1) * 5 * ' ', end='', sep='')
        print('-' * level, self.wartosc, end='', sep='')
        if len(str(self.wartosc).split('.')[1]) == 1:
            print(' ', end='', sep='')
        if self.lewy:
            self.lewy.WYSWIETL(level + 1)
        if self.prawy:
            self.prawy.WYSWIETL(level + 1, is_right=self.lewy is not None)
        if (not self.lewy) and (not self.prawy):
            print()

    def MINIMUM(self):
        najmniejszy = self
        while najmniejszy.lewy is not None:
            najmniejszy = najmniejszy.lewy
        return najmniejszy.wartosc

    def MAXIMUM(self):
        najwiekszy = self
        while najwiekszy.prawy is not None:
            najwiekszy = najwiekszy.prawy
        return najwiekszy.wartosc

    def SEARCH(self, szukane):
        if self.wartosc == szukane:
            return True
        elif self.wartosc < szukane:
            if self.lewy is None:
                return False
            return self.lewy.SEARCH(szukane)
        elif self.wartosc > szukane:
            if self.prawy is None:
                return False
            return self.prawy.SEARCH(szukane)

class Tree:
    def __init__(self, length):
        self.length = length
        self.wezly = [Wezel(i) for i in np.arange(0.5, length + 0.5, 1.0)]

    def wstaw(self,wartosc):
        self.wezly[math.floor(wartosc)].INSERT(wartosc)

    def najwiekszy(self, wartosc):
        return self.wezly[math.floor(wartosc)].MAXIMUM()

    def najmniejszy(self, wartosc):
        return self.wezly[math.floor(wartosc)].MINIMUM()

    def szukaj(self, wartosc):
        return self.wezly[math.floor(wartosc)].SEARCH(wartosc)

    def wyswietl_tablice(self):
        for wezel in self.wezly:
            if wezel.lewy is not None or wezel.prawy is not None:
                wezel.WYSWIETL()


# if __name__ == "__main__":
#
#     drzewa = Tree()
#
#     l = 100
#     elementy = [random.choice([round(i,2) for i in np.arange(0.01, 100.0, 0.01)]) for z in range(l)]
#
#     liczby_testowe = [1.3, 0.4, 1.6, 3.4, 2.6, 2.7, 3.7]
#
#     for i in range(len(drzewa.wezly)):
#         for j in elementy:
#             if abs(drzewa.wezly[i].wartosc - j) < 0.5:
#                 drzewa.wezly[i].INSERT(j)
#
#     drzewa.wyswietl_tablice()