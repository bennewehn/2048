import numpy as np
import random
import getch

class Game:
    def __init__(self, n):
        self.board = np.zeros(shape=(n, n))
        self.score = 0

    def print(self):
        print('Score: ' + str(self.score))
        print(self.board)

    # adds new tile to random free position
    # 1. get all zero vals
    # 2. get random position
    # 3. add 2 or 4
    def __addTile(self):
        free = [(x, y) for x, e in enumerate(self.board) for y, val in enumerate(e) if val == 0]
        if len(free) > 0:
            pos = int(random.random() * len(free))
            val = 2 if random.random() < 0.9 else 4
            self.board[free[pos]] = val

    def __slide(self, row):
        arr = [e for e in row if e != 0]
        zero = np.zeros(len(row) - len(arr))
        return np.append(zero, arr)

    def __merge(self, row):
        for i in range(len(row) - 1, 0, -1):
            if row[i] == row[i - 1]:
                row[i] = row[i - 1] * 2
                self.score += row[i]
                row[i - 1] = 0
        return row

    def __slideAndMerge(self, row):
        return self.__slide(self.__merge(self.__slide(row)))

    def move(self, direction):
        for i in range(len(self.board)):
            match direction:
                case 'up':
                    self.board[:, i] = np.flip(self.__slideAndMerge(np.flip(self.board[:, i])))

                case 'right':
                    self.board[i] = self.__slideAndMerge(self.board[i])

                case 'down':
                    self.board[:, i] = self.__slideAndMerge(self.board[:, i])

                case 'left':
                    self.board[i] = np.flip(self.__slideAndMerge(np.flip(self.board[i])))
    
    def hasLost(self):
        if 0 in self.board:
            return False 

        for i in range(len(self.board)):
            for j in range(len(self.board)-1):
                if self.board[i][j]==self.board[i][j+1] or self.board[j][i]==self.board[j+1][i]:
                    return False
        return True

    def play(self):
        self.__addTile()
        self.__addTile()
        while True:
            self.print()
            if getch.getch() == '\x1b' and getch.getch() == '[':
                char = getch.getch()
                if char == 'A':
                    self.move('up')
                elif char == 'B':
                    self.move('down')
                elif char == 'C':
                    self.move('right')
                elif char == 'D':
                    self.move('left')

            if self.hasLost():
                print("lost")
                break
            self.__addTile()