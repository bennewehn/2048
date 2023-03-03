import numpy as np
import random

class Game:
    def __init__(self):
        self.board = np.zeros(shape=(4, 4))
        pass
    
    def print(self):
        print(self.board)

    def addTile(self):
        # 1. get all zero vals
        # 2. get random position
        # 3. get random value
        # 4. add tile
        free = [(x, y) for x, e in enumerate(self.board) for y, val in enumerate(e) if val == 0] 
        if len(free) > 0:
            pos = int(random.random() * len(free))
            val = 2 if random.random() < 0.9 else 4
            self.board[free[pos]] = val

    def slide(self, row):
        arr = [e for e in row if e != 0]
        zero = np.zeros(4 - len(arr))
        return np.append(zero, arr)

    
    
    
    def combine(self, row):
        pass