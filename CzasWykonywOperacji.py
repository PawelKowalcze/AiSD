from ZlozoneStruktDanych import Tree
import time
import random
import numpy as np

if __name__ == '__main__':

    numbers = [25, 50, 100, 500, 1000, 2000, 3000]
    for number in numbers:
        n = 25
        trees = Tree(n)
        elements = [random.choice([round(i, 2) for i in np.arange(0.01, n, 0.01)]) for z in range(number)]
        stime = time.time()
        for i in range(len(trees.nodes)):
            for j in elements:
                if abs(trees.nodes[i].value - j) < 0.5:
                    trees.nodes[i].INSERT(j)
        etime = time.time()
        howMuch = 100000
        maxstime = time.time()
        for i in range(howMuch):
            maximium = trees.max(random.uniform(.00,10.00))
        maxtime = time.time()

        minstime = time.time()
        for i in range(howMuch):
            minimum = trees.min(random.uniform(.00,10.00))
        mintime = time.time()

        searchedNum = round(random.uniform(0.00,10.00), 2)

        sstime = time.time()
        for i in range(howMuch):
            is_there = trees.search(searchedNum)
        estime = time.time()

        print(f"Time insert for each of {number} elements: {(etime - stime)} s")
        print(f"Time maximum for each of {number} elements:: {(maxtime - maxstime)} s")
        print(f"Time minimum for each of {number} elements:: {(mintime - minstime)} s")
        print(f"Time search for each of {number} elements:: {(estime - sstime)} s")
        print(f"Time insert for {number} elements: {(etime - stime) * number} s")
        print(f"Time maximum for {number} elements:: {(maxtime - maxstime) * number} s")
        print(f"Time minimum for {number} elements:: {(mintime - minstime) * number} s")
        print(f"Time search for {number} elements:: {(estime - sstime) * number} s")
        print('_' * 50)