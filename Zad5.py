import random
Board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def PrintBoard():
    for i in range(0, 3):
        print("-------")
        for j in range(0, 3):
            print("|", end=Board[i][j])
        print("|")
    print("-------")


def didSbWin(player):
    if player % 2 == 0:
        name = 'O'
    else:
        name = 'X'

    if Board[0][0] == Board[1][1] == Board[2][2] != " " or Board[2][0] == Board[1][1] == Board[0][2] != " ":
        return name

    for i in range(0, 3):
        if Board[0][i] == Board[1][i] == Board[2][i] != " " or Board[i][0] == Board[i][1] == Board[i][2] != " ":
            return name
    return 0


def PlayerMove(Player):
    while True:
        x = int(input("Choose your x coordinate: (1-3)\n"))
        y = int(input("Choose your y coordinate: (1-3)\n"))
        if 1 <= x <= 3 and 1 <= y <= 3:
            if Board[y - 1][x - 1] == " ":
                if Player % 2 == 0:
                    Board[y - 1][x - 1] = "O"
                    PrintBoard()
                    if didSbWin(Player) != 0:
                        print('WINNER: ' + str(didSbWin(Player)) + ' (Player 1)')
                        return 10
                    break
                else:
                    Board[y - 1][x - 1] = "X"
                    PrintBoard()
                    if didSbWin(Player) != 0:
                        print('WINNER: ' + str(didSbWin(Player)) + ' (Player 2)')
                        return 10
                    break
            else:
                print('Index taken. Try again\n')
        else:
            print('Wrong index. Try again\n')


def ComputerMove(Player):
    while True:
        if Player % 2 == 0:
            x = int(input("Choose your x coordinate: (1-3)\n"))
            y = int(input("Choose your y coordinate: (1-3)\n"))
        else:
            while True:
                x = random.randint(1, 3)
                y = random.randint(1, 3)
                if Board[y - 1][x - 1] == " ":
                    break
        if 1 <= x <= 3 and 1 <= y <= 3:
            if Board[y - 1][x - 1] == " ":
                if Player % 2 == 0:
                    Board[y - 1][x - 1] = "O"
                    PrintBoard()
                    if didSbWin(Player) != 0:
                        print('WINNER: ' + str(didSbWin(Player)) + ' (Player)')
                        return 10
                    break
                else:
                    Board[y - 1][x - 1] = "X"
                    PrintBoard()
                    if didSbWin(Player) != 0:
                        print('WINNER: ' + str(didSbWin(Player)) + ' (Computer)')
                        return 10
                    break
            else:
                print('Index taken. Try again\n')
        else:
            print('Wrong index. Try again\n')


playerIndex = 0
gameplay = int(input('HI. This is game Tic-Tac-Toe. Would you like to play? (1 - yes, 2 - no)\n'))
while True:
    gameMode = int(input('Which game would you like to choose? (1 - Player vs Player, 2 - Player vs Computer)\n'))
    while True:
        if gameplay == 1:
            if gameMode == 1:
                if PlayerMove(playerIndex) == 10:
                    playerIndex = 9
                playerIndex += 1
                if playerIndex >= 9:
                    if playerIndex == 9:
                        print('Its a tie \n')
                    gameplay = int(input('Would you like to play again? 1 - yes, 2 - no\n'))
                    Board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                    playerIndex = 0
                    break
            elif gameMode == 2:
                if ComputerMove(playerIndex) == 10:
                    playerIndex = 9
                playerIndex += 1
                if playerIndex >= 9:
                    if playerIndex == 9:
                        print('Its a tie \n')
                    gameplay = int(input('Would you like to play again? 1 - yes, 2 - no\n'))
                    Board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                    playerIndex = 0
                    break
            else:
                print('Wrong number. Choose gameMode again\n')
                break

        elif gameplay == 2:
            # print('Game has ended\n')
            break
        else:
            gameplay = int(input('Incorrect option - try again. (1 - yes, 2 - no)\n'))

    if gameplay == 2:
        print('Game has ended\n')
        break
