from zad3 import Wezel, Tree
import time
import random
import numpy as np

if __name__ == '__main__':

    liczby = [25, 50, 100, 500, 1000, 2500, 5000, 7500]
    for liczba in liczby:
        n = 20
        drzewa = Tree(n)

        elementy = [random.choice([round(i, 2) for i in np.arange(0.01, n, 0.01)]) for z in range(liczba)]
        # elementy = [(round(i, 2) for i in np.arange(0.01, 25.0, 0.01)) for i in range(l)]

        stime = time.time()
        for i in range(len(drzewa.wezly)):
            for j in elementy:
                if abs(drzewa.wezly[i].wartosc - j) < 0.5:
                    drzewa.wezly[i].INSERT(j)
        etime = time.time()

        how_much = 100000
        maxstime = time.time()
        for i in range(how_much):
            maximium = drzewa.najwiekszy(random.uniform(.00,10.00))
        maxtime = time.time()

        minstime = time.time()
        for i in range(how_much):
            minimum = drzewa.najmniejszy(random.uniform(.00,10.00))
        mintime = time.time()

        szukana_liczba = round(random.uniform(0.00,10.00), 2)

        sstime = time.time()
        for i in range(how_much):
            is_there = drzewa.szukaj(szukana_liczba)
        estime = time.time()

        print(f"Czas dla insert dla {liczba} elementów: {(etime - stime)} sekund")
        print(f"Czas dla maximum dla {liczba} elementów:: {(maxtime - maxstime)/how_much} sekund")
        print(f"Czas dla minimum dla {liczba} elementów:: {(mintime - minstime)/how_much} sekund")
        print(f"Czas dla search dla {liczba} elementów:: {(estime - sstime)/how_much} sekund")
        print('*'*25)
