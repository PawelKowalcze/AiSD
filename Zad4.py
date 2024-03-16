try:
    print(1/0)
except ZeroDivisionError:
    print("Nie dziel przez zero")

try:
    L = [2,2.3]
    print(L[3])
except IndexError:
    print("Patrz na indexy")

try:
    print(b)
except NameError:
    print("Nieodpowiednia nazwa")