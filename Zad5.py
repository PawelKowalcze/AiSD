Board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def PrintBoard():
    for i in range(0, 3):
        print("-------")
        for j in range(0, 3):
            print("|", end=Board[i][j])
        print("|")
    print("-------")


def PlayerMove(Turn):
    x = int(input("Choose your x coordinate: "))
    y = int(input("Choose your y coordinate: "))
    if Turn % 2 == 0:
        Board[y - 1][x - 1] = "X"
    else:
        Board[y - 1][x - 1] = "O"

    PrintBoard()
    print()


Turn = 0
while True:
    PlayerMove(Turn)
    Turn += 1
