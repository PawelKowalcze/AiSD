from random import randint, sample


class LOTTO:
    numbers = []

    def __init__(self, numbers):
        if len(numbers) != 5 and len(numbers) != 6: # od teraz len(self.numbers) bedzie mowic czy to 5 czy 6 elementow
            print("List must contain 5 or 6 elements")
            exit()
        for number in numbers:
            if number < 0 or number > 48:
                print("Numbers must be in <0;48> interval")
                exit()
        self.numbers = sorted(numbers)

    def SPRAWDZ(self, other):
        return self.numbers == other.numbers

    def GRAJ(self):
        # Zakladam, ze gramy juz wprowadzonymi wartosciami, np:
        # zaklad = lotto([1,4,42, 13, 7]) <- gramy tymi wartosciami, to sa nasze liczby
        # lotto.GRAJ()
        winning_ticket = LOTTO(sample(range(0, 48), len(self.numbers))) # losujemy zwycieskie liczby

        if self.SPRAWDZ(winning_ticket):
            print("You win!")
        else:
            print("Try again, you'll surely win next time.")


# TESTOWANKO
zestaw1 = LOTTO([1, 1, 1, 3, 8])
zestaw2 = LOTTO([8, 3, 1, 1, 1])
print(zestaw1.SPRAWDZ(zestaw2))

zestaw2.GRAJ()

# KONIEC TESTOWANKA

# Wylosuje 1000 zestawów NIEZALEZNIE od klasy LOTTO - nie rozumiem dokladnie polecenia xd
zestawy = []
for i in range(1000):
    zestawy.append(sorted(sample(range(0, 48), 6))) #sortuje pojedyncze od razu

occurrences = []
for i in range(len(zestawy)):
    occurrence_num = zestawy.count(zestawy[i])
    occurrences.append([occurrence_num, zestawy[i]])


occurrences.sort(reverse=True)
print(occurrences)

file_name = str(occurrences[0]) + str(occurrences[1])
f = open(f"{file_name}.txt", 'w')
for element in occurrences:
    f.writelines(f"{element}\n")

f.close()