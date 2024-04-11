import random
class LOTTO:
    zestaw = []
    def __init__(self, numbers):
        if len(numbers) == 6: #tam było dla 5 lub 6 - ja robię tylko dla 6
            self.zestaw = sorted(numbers)

'''
#do testowania czy działa klasa
n = 5
dane = random.sample(range(0,48),n)
dane2 = random.sample(range(0,48),n)
dane3 = [1,2,3,4,5,6]
dane4 = [5,6,3,4,2,1]
tablica = LOTTO(dane)
tablica2 = LOTTO(dane2)

tablica3 = LOTTO(dane3)
tablica4 = LOTTO(dane4)

print(SPRAWDZ(tablica3, tablica4))
'''


def SPRAWDZ(l1, l2):
    if l1 == l2:
        return True


def GRAJ(user_ticket):
    is_win = SPRAWDZ(user_ticket, winning_ticket)
    if is_win:
        print("You're a winner")
    else:
        print("Sorry, you didn't win, try again")

if __name__ == "__main__":

    user_input = input("Enter six unique numbers separated by space (from 0 to 48): ").split()
    user_ticket = LOTTO([int(i) for i in user_input])

    winning_ticket = LOTTO(random.sample(range(0, 48), 6))  # random.sample() - z danego przedziału losuje niepowtarzające się liczby

    GRAJ(user_ticket)

    SPRAWDZ(user_ticket, winning_ticket)

    wylosowane_zestawy = []
    for i in range(0, 999):
        wylosowane_zestawy.append(LOTTO(random.sample(range(0, 48), 6)))

    wystapienia = []
    for i in wylosowane_zestawy:
        dane = [wylosowane_zestawy.count(i), i.zestaw]
        wystapienia.append(dane)

    wystapienia.sort(reverse=True)

    name = str(wystapienia[0]) + str(wystapienia[1])
    zapis = open(f"{name}.txt", 'w')
    for i in wystapienia:
        zapis.writelines(f"{i}\n")

    zapis.close()


