import math
import numpy as np
import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def INSERT(self, data):
        if self.value is None:
            self.value = data
            return
        elif self.value == data:
            return
        else:
            if data < self.value:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.INSERT(data)
            elif self.value < data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.INSERT(data)

    def SHOW(self, level=0, is_right=False):
        if is_right:
            print(' ' * 4, (level - 1) * 5 * ' ', end='', sep='')
        print('-' * level, self.value, end='', sep='')
        if len(str(self.value).split('.')[1]) == 1:
            print(' ', end='', sep='')
        if self.left:
            self.left.SHOW(level + 1)
        if self.right:
            self.right.SHOW(level + 1, is_right=self.left is not None)
        if (not self.left) and (not self.right):
            print()

    def MINIMUM(self):
        min = self
        while min.left is not None:
            min = min.left
        return min.value

    def MAXIMUM(self):
        max = self
        while max.right is not None:
            max = max.right
        return max.value

    def SEARCH(self, searched):
        if self.value == searched:
            return True
        elif self.value < searched:
            if self.left is None:
                return False
            return self.left.SEARCH(searched)
        elif self.value > searched:
            if self.right is None:
                return False
            return self.right.SEARCH(searched)

class Tree:
    def __init__(self, length):
        self.length = length
        self.nodes = [Node(i) for i in np.arange(0.5, length + 0.5, 1.0)]

    def insert(self,value):
        self.nodes[math.floor(value)].INSERT(value)

    def max(self, value):
        return self.nodes[math.floor(value)].MAXIMUM()

    def min(self, value):
        return self.nodes[math.floor(value)].MINIMUM()

    def search(self, value):
        return self.nodes[math.floor(value)].SEARCH(value)

    def SHOW_arrays(self):
        for Node in self.nodes:
            if Node.left is not None or Node.right is not None:
                Node.SHOW()


if __name__ == "__main__":
     trees = Tree(100)
     l = 100
     elements = [random.choice([round(i,2) for i in np.arange(0.01, 100.0, 0.01)]) for z in range(l)]
     for i in range(len(trees.nodes)):
         for j in elements:
             if abs(trees.nodes[i].value - j) < 0.5:
                 trees.nodes[i].INSERT(j)
     trees.SHOW_arrays()