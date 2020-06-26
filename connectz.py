# Written by Jun-te Kim
# 07519530549
# juntekim@gmail.com
import sys


class Game():
    def __init__(self, setupInstructions):
        self.width, self.height, self.winCondition \
                = self.initialise(setupInstructions)
        self.grid = []
        self.winner = 0
        self.maxMoves = self.width * self.height
        # Makes a 2 dimensional array representing the game board
        # Intially filled with 0's denoting empty space and later
        # 1's and 2's representing each player.
        for i in range(self.width):
            temp = []
            for j in range(self.height):
                temp.append(0)
            self.grid.append(temp)

    def addCounter(self, column, player):
        """
        Validates and updates the grid based on player move

        Checks for win condition and updates self.winner
        """
        playerID = self.getPlayerID(player)

        if column <= self.width and column > 0:
            counter = 0

            while counter < self.height:
                if self.grid[column-1][counter] == 0:
                    self.grid[column-1][counter] = playerID
                    self.printGrid()
                    if self.winner == 0:
                        if self.checkWin(column-1, counter) is True:
                            self.winner = playerID
                    return
                counter = counter + 1

            # Illegal row
            print(5)
            exit()
        else:
            # Illegal column
            print(6)
            exit()

        self.hasEmptySpace = False

    def checkWin(self, x, y):
        if self.checkHorizontal(x, y) is True:
            return True
        if self.checkVertical(x, y) is True:
            return True
        return self.checkDiagonal(x, y)

    def checkHorizontal(self, x, y):
        """
        Checks to see if there is a win case in the horizontal direction

        Return True: if win condition found within the horizontal
        direction

        Return False: if win condition was not found within the
        horizontal direction
        """
        counter = 1
        player = self.grid[x][y]
        offset = 1
        if counter == self.winCondition:
            return True
        if x+offset < self.width-1:
            while self.grid[x+offset][y] == player:
                counter = counter + 1
                if counter >= self.winCondition:
                    return True
                offset = offset + 1
                if x+offset == self.width:
                    break

        offset = 1
        if x-offset > -1:
            while self.grid[x-offset][y] == player:
                counter = counter + 1
                if counter >= self.winCondition:
                    return True
                offset = offset + 1
                if x-offset == -1:
                    break

        return False

    def checkVertical(self, x, y):
        """
        Checks to see if there is a win case in the vertical direction

        Retrun True: if win condition found within the vertical
        direction

        Return False: if win condition was not found within the
        vertical direction
        """
        counter = 1
        player = self.grid[x][y]
        offset = 1
        if y-offset > -1:
            while self.grid[x][y-offset] == player:
                counter = counter + 1
                if counter >= self.winCondition:
                    return True
                offset = offset + 1
                if y-offset == -1:
                    break
        return False

    def checkDiagonal(self, x, y):
        """
        Checks to see if there is a win case in both the diagonal
        direction.

        Return True: if win condition found within the diagonal
        Return False: if win condition was not found within the diagonal
        """
        counter = 1
        player = self.grid[x][y]
        offset = 1
        if x+offset < self.width-1 and y+offset < self.height-1:
            while self.grid[x+offset][y+offset] == player:
                counter = counter + 1
                if counter >= self.winCondition:
                    return True
                offset = offset + 1
                if x+offset == self.width or y+offset == self.height:
                    break
        offset = 1
        if x-offset > -1 and y-offset > -1:
            while self.grid[x-offset][y-offset] == player:
                counter = counter + 1
                if counter >= self.winCondition:
                    return True
                offset = offset + 1
                if x-offset == -1 or y-offset == -1:
                    break

        counter = 1
        offset = 1

        if x+offset < self.width-1 and y-offset > -1:
            while self.grid[x+offset][y-offset] == player:
                counter = counter + 1
                if counter >= self.winCondition:
                    return True
                offset = offset + 1
                if x+offset == self.width or y-offset == -1:
                    break
        offset = 1
        if x-offset > -1 and y+offset < self.height-1:
            while self.grid[x-offset][y+offset] == player:
                counter = counter + 1
                if counter >= self.winCondition:
                    return True
                offset = offset + 1
                if x-offset == -1 or y-offset == -1:
                    break

        return False

    def getPlayerID(self, number):
        """
        Returns the player number based on which file line the program
        is on
        """
        ID = number % 2
        if ID == 0:
            return 2
        else:
            return 1

    def initialise(self, setup):
        """
        Initilises the game by setting up the width, height and win
        condition variable with error checking
        """
        setup = setup.split(" ")
        if len(setup) != 3:
            # Invalid File
            print(8)
            exit()
        else:
            width = int(setup[0])
            height = int(setup[1])
            winCondition = int(setup[2])
            if winCondition > width and winCondition > height \
                    or winCondition < 1:
                # Illegal Game
                print(7)
                exit()
            if width > 0 and height > 0 and winCondition > 0:
                return width, height, winCondition
            else:
                # Setup numbers are not greater than 0 so invalid format
                # Invalid file
                print(8)
                exit()

    def printGrid(self):
        """
        Allows the user to see the current state of self.grid
        For development purposes only.
        """
        print()
        print("-------------------------------------------")
        for i in range(self.height):
            for j in range(self.width):
                print(self.grid[j][self.height-i-1], end="")
            print()
        print("-------------------------------------------")
        print()


if __name__ == "__main__":
    moveNo = 0
    if len(sys.argv) != 2:
        print("Provide one input file")
        exit()
    try:
        with open(sys.argv[1], 'r') as f:
            for moveNo, line in enumerate(f.read().splitlines()):
                if moveNo == 0:
                    board = Game(line)
                else:
                    nextMove = int(line)
                    if nextMove > 0:
                        if board.winner == 0:
                            board.addCounter(nextMove, moveNo)
                        else:
                            # Illegal continue. Winner established
                            print(4)
                            exit()
                    else:
                        # Move is not a postive interger
                        # wrong file format
                        print(8)
                        exit()

        if board.winner == 0 and moveNo < board.maxMoves:
            # Game is incomplete. Game is neither won or drawn
            print(3)
            exit()
        else:
            # Prints out winner or 0 for draw
            print(board.winner)
            exit()

    except FileNotFoundError:
        print(9)
    except ValueError:
        # Invalide file - The file is opened but does not conform the
        # format
        print(8)
