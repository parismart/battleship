import numpy as np

class Board():

    def __init__(self,id):
        self.id = id
        self.board = np.full((10,10)," ")
        self.board_machine = np.full((10,10)," ")
        self.inv = []
        self.set_ships()

    def fire(self,coord_x, coord_y):
        if (coord_x, coord_y) not in self.inv:
            self.board_machine[coord_x, coord_y] = '1'
            self.board[coord_x, coord_y] = '1'
            print("Water")
            return(0)
        else:
            self.board_machine[coord_x, coord_y] = 'X'
            self.board[coord_x, coord_y] = 'X'
            self.inv.remove((coord_x, coord_y))
            print("Match")
            return(1)

    def set_ships(self):
        self.set_ship_4()
        self.set_ships_3()
        self.set_ships_2()
        self.set_ships_1()

    def set_ships_1(self):
        for i in range(4):
            x, y = self.rand_coord()
            self.board[x,y] = "O"
            self.inv += [(x,y)]

    def set_ships_2(self):
        for i in range(3):
            x, y = self.rand_coord()
            z = self.rand_orient_2(x,y)
            if z == 'N':
                self.board[(x,x-1),(y)] = "O"
                self.inv += [(x,y), (x-1,y)]
            elif z == 'S':
                self.board[(x,x+1),(y)] = "O"
                self.inv += [(x,y), (x+1,y)]
            elif z == 'E':
                self.board[(x),(y,y+1)] = "O"
                self.inv += [(x,y), (x,y+1)]
            elif z == 'W':
                self.board[(x),(y,y-1)] = "O"
                self.inv += [(x,y), (x,y-1)]

    def set_ships_3(self):
        for i in range(2):
            x, y = self.rand_coord()
            z = self.rand_orient_3(x,y)
            if z == 'N':
                self.board[(x,x-1,x-2),(y)] = "O"
                self.inv += [(x,y), (x-1,y), (x-2,y)]
            elif z == 'S':
                self.board[(x,x+1,x+2),(y)] = "O"
                self.inv += [(x,y), (x+1,y), (x+2,y)]
            elif z == 'E':
                self.board[(x),(y,y+1,y+2)] = "O"
                self.inv += [(x,y), (x,y+1), (x,y+2)]
            elif z == 'W':
                self.board[(x),(y,y-1,y-2)] = "O"
                self.inv += [(x,y), (x,y-1), (x,y-2)]

    def set_ship_4(self):
        x = np.random.randint(10)
        y = np.random.randint(10)
        z = self.rand_orient_4(x,y)
        if z == 'N':
            self.board[(x,x-1,x-2,x-3),(y)] = "O"
            self.inv += [(x,y), (x-1,y), (x-2,y), (x-3,y)]
        elif z == 'S':
            self.board[(x,x+1,x+2,x+3),(y)] = "O"
            self.inv += [(x,y), (x+1,y), (x+2,y), (x+3,y)]
        elif z == 'E':
            self.board[(x),(y,y+1,y+2,y+3)] = "O"
            self.inv += [(x,y), (x,y+1), (x,y+2), (x,y+3)]
        elif z == 'W':
            self.board[(x),(y,y-1,y-2,y-3)] = "O"
            self.inv += [(x,y), (x,y-1), (x,y-2), (x,y-3)]

    def rand_coord(self):
        while True:
            x = np.random.randint(10)
            y = np.random.randint(10)
            if 0 not in [x,y] and 9 not in [x,y]:
                if 'O' not in [self.board[x,y], self.board[x-1,y],self.board[x+1,y],\
                self.board[x,y+1],self.board[x,y-1],self.board[x-1,y-1],self.board[x+1,y+1],\
                self.board[x-1,y+1],self.board[x+1,y-1]]:
                    break
            if x == 0:
                if y != 9 and y != 0:
                    if 'O' not in [self.board[x,y],self.board[x+1,y],self.board[x,y+1],\
                    self.board[x,y-1],self.board[x+1,y+1],self.board[x+1,y-1]]:
                        break
                if y == 0:
                    if 'O' not in [self.board[x,y],self.board[x+1,y],self.board[x,y+1],self.board[x+1,y+1]]:
                        break
                if y == 9:
                    if 'O' not in [self.board[x,y],self.board[x+1,y],self.board[x,y-1],self.board[x+1,y-1]]:
                        break
            if x == 9:
                if y != 9 and y != 0:
                    if 'O' not in [self.board[x,y], self.board[x-1,y],self.board[x,y+1],\
                    self.board[x,y-1],self.board[x-1,y-1],self.board[x-1,y+1]]:
                        break
                if y == 0:
                    if 'O' not in [self.board[x,y],self.board[x-1,y],self.board[x,y+1],self.board[x-1,y+1]]:
                        break
                if y == 9:
                    if 'O' not in [self.board[x,y],self.board[x-1,y],self.board[x,y-1],self.board[x-1,y-1]]:
                        break
            if y == 0:
                if x != 9 and x != 0:
                    if 'O' not in [self.board[x,y], self.board[x-1,y],self.board[x+1,y],\
                    self.board[x,y+1],self.board[x+1,y+1],self.board[x-1,y+1]]:
                        break
                if x == 0:
                    if 'O' not in [self.board[x,y],self.board[x,y+1],self.board[x+1,y],self.board[x+1,y+1]]:
                        break
                if x == 9:
                    if 'O' not in [self.board[x,y],self.board[x,y+1],self.board[x-1,y],self.board[x-1,y+1]]:
                        break
            if y == 9:
                if x != 9 and x != 0:
                    if 'O' not in [self.board[x,y], self.board[x-1,y],self.board[x+1,y],\
                    self.board[x,y-1],self.board[x-1,y-1],self.board[x+1,y-1]]:
                        break
                if x == 0:
                    if 'O' not in [self.board[x,y],self.board[x,y-1],self.board[x+1,y],self.board[x+1,y-1]]:
                        break
                if x == 9:
                    if 'O' not in [self.board[x,y],self.board[x,y-1],self.board[x-1,y],self.board[x-1,y-1]]:
                        break
        return(x,y)

    def rand_orient_2(self,x,y):
        while True:
            z = np.random.choice(['N','S','E','W'])
            if (z == 'N' and x-1 >= 0):
                if x-1 == 0:
                    break
                elif self.board[x-2,y] != 'O':
                    if y != 9 and y != 0:
                        if 'O' not in [self.board[x-2,y-1],self.board[x-2,y+1]]:
                            break
                    elif y == 9:
                        if self.board[x-2,y-1] != 'O':
                            break
                    elif y == 0:
                        if self.board[x-2,y+1] != 'O':
                            break
            elif (z == 'S' and x+1 <= 9):
                if x+1 == 9:
                    break
                elif self.board[x+2,y] != 'O':
                    if y != 9 and y != 0:
                        if 'O' not in [self.board[x+2,y-1],self.board[x+2,y+1]]:
                            break
                    elif y == 9:
                        if self.board[x+2,y-1] != 'O':
                            break
                    elif y == 0:
                        if self.board[x+2,y+1] != 'O':
                            break
            elif (z == 'E' and y+1 <= 9):
                if y+1 == 9:
                    break
                elif self.board[x,y+2] != 'O':
                    if x != 9 and x != 0:
                        if 'O' not in [self.board[x-1,y+2],self.board[x+1,y+2]]:
                            break
                    elif x == 9:
                        if self.board[x-1,y+2] != 'O':
                            break
                    elif x == 0:
                        if self.board[x+1,y+2] != 'O':
                            break
            elif (z == 'W' and y-1 >= 0):
                if y-1 == 0:
                    break
                elif self.board[x,y-2] != 'O':
                    if x != 9 and x != 0:
                        if 'O' not in [self.board[x-1,y-2],self.board[x+1,y-2]]:
                            break
                    elif x == 9:
                        if self.board[x-1,y-2] != 'O':
                            break
                    elif x == 0:
                        if self.board[x+1,y-2] != 'O':
                            break
        return(z)

    def rand_orient_3(self,x,y):
        while True:
            z = np.random.choice(['N','S','E','W'])
            if (z == 'N' and x-2 >= 0):
                if self.board[x-2,y] != 'O' and x-2 == 0:
                    if y != 9 and y != 0:
                        if 'O' not in [self.board[x-2,y-1],self.board[x-2,y+1]]:
                            break
                    elif y == 9:
                        if self.board[x-2,y-1] != 'O':
                            break
                    elif y == 0:
                        if self.board[x-2,y+1] != 'O':
                            break
                elif self.board[x-3,y] != 'O':
                    if y != 9 and y != 0:
                        if 'O' not in [self.board[x-3,y-1],self.board[x-3,y+1]]:
                            break
                    elif y == 9:
                        if self.board[x-3,y-1] != 'O':
                            break
                    elif y == 0:
                        if self.board[x-3,y+1] != 'O':
                            break
            elif (z == 'S' and x+2 <= 9):
                if self.board[x+2,y] != 'O' and x+2 == 9:
                    if y != 9 and y != 0:
                        if 'O' not in [self.board[x+2,y-1],self.board[x+2,y+1]]:
                            break
                    elif y == 9:
                        if self.board[x+2,y-1] != 'O':
                            break
                    elif y == 0:
                        if self.board[x+2,y+1] != 'O':
                            break
                elif self.board[x+3,y] != 'O':
                    if y != 9 and y != 0:
                        if 'O' not in [self.board[x+3,y-1],self.board[x+3,y+1]]:
                            break
                    elif y == 9:
                        if self.board[x+3,y-1] != 'O':
                            break
                    elif y == 0:
                        if self.board[x+3,y+1] != 'O':
                            break
            elif (z == 'E' and y+2 <= 9):
                if self.board[x,y+2] != 'O' and y+2 == 9:
                    if x != 9 and x != 0:
                        if 'O' not in [self.board[x-1,y+2],self.board[x+1,y+2]]:
                            break
                    elif x == 9:
                        if self.board[x-1,y+2] != 'O':
                            break
                    elif x == 0:
                        if self.board[x+1,y+2] != 'O':
                            break
                elif self.board[x,y+3] != 'O':
                    if x != 9 and x != 0:
                        if 'O' not in [self.board[x-1,y+3],self.board[x+1,y+3]]:
                            break
                    elif x == 9:
                        if self.board[x-1,y+3] != 'O':
                            break
                    elif x == 0:
                        if self.board[x+1,y+3] != 'O':
                            break
            elif (z == 'W' and y-2 >= 0):
                if self.board[x,y-2] != 'O' and y-2 == 9:
                    if x != 9 and x != 0:
                        if 'O' not in [self.board[x-1,y-2],self.board[x+1,y-2]]:
                            break
                    elif x == 9:
                        if self.board[x-1,y-2] != 'O':
                            break
                    elif x == 0:
                        if self.board[x+1,y-2] != 'O':
                            break
                elif self.board[x,y-3] != 'O':
                    if x != 9 and x != 0:
                        if 'O' not in [self.board[x-1,y-3],self.board[x+1,y-3]]:
                            break
                    elif x == 9:
                        if self.board[x-1,y-3] != 'O':
                            break
                    elif x == 0:
                        if self.board[x+1,y-3] != 'O':
                            break
        return(z)

    def rand_orient_4(self,x,y):
        while True:
            z = np.random.choice(['N','S','E','W'])
            if (z == 'N' and x-3 >= 0):
                if 'O' not in [self.board[x-3,y],self.board[x-2,y],self.board[x-1,y]]:
                    break
            elif (z == 'S' and x+3 <= 9):
                if 'O' not in [self.board[x+3,y],self.board[x+2,y],self.board[x+1,y]]:
                    break
            elif (z == 'E' and y+3 <= 9):
                if 'O' not in [self.board[x,y+3],self.board[x,y+2],self.board[x,y+1]]:
                    break
            elif (z == 'W' and y-3 >= 0):
                if 'O' not in [self.board[x,y-3],self.board[x,y-2],self.board[x,y-1]]:
                    break
        return(z)
