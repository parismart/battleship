import numpy as np

class Board():

    def __init__(self,ships=0):
        self.board = np.full((10,10)," ")
        self.board_machine = np.full((10,10)," ")
        self.items = ["1","2","3","4"]
        self.inv = []
        self.ships = ships
        self.set_ships()

    def fire(self,x, y):
        if (x, y) not in self.inv:
            self.board_machine[x, y] = 'W'
            self.board[x, y] = 'W'
            print("Water")
            return(0)
        else:
            self.board_machine[x, y] = 'X'
            self.board[x, y] = 'X'
            self.set_border(x, y)
            self.inv.remove((x, y))
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
            self.board[x,y] = "1"
            self.inv += [(x,y)]
            if self.ships == 1:
                print(self.board)

    def set_ships_2(self):
        for i in range(3):
            x, y = self.rand_coord()
            z = self.rand_orient_2(x,y)
            if z == 'N':
                self.board[(x,x-1),(y)] = "2"
                self.inv += [(x,y), (x-1,y)]
            elif z == 'S':
                self.board[(x,x+1),(y)] = "2"
                self.inv += [(x,y), (x+1,y)]
            elif z == 'E':
                self.board[(x),(y,y+1)] = "2"
                self.inv += [(x,y), (x,y+1)]
            elif z == 'W':
                self.board[(x),(y,y-1)] = "2"
                self.inv += [(x,y), (x,y-1)]
            if self.ships == 1:
                print(self.board)

    def set_ships_3(self):
        for i in range(2):
            x, y = self.rand_coord()
            z = self.rand_orient_3(x,y)
            if z == 'N':
                self.board[(x,x-1,x-2),(y)] = "3"
                self.inv += [(x,y), (x-1,y), (x-2,y)]
            elif z == 'S':
                self.board[(x,x+1,x+2),(y)] = "3"
                self.inv += [(x,y), (x+1,y), (x+2,y)]
            elif z == 'E':
                self.board[(x),(y,y+1,y+2)] = "3"
                self.inv += [(x,y), (x,y+1), (x,y+2)]
            elif z == 'W':
                self.board[(x),(y,y-1,y-2)] = "3"
                self.inv += [(x,y), (x,y-1), (x,y-2)]
            if self.ships == 1:
                print(self.board)

    def set_ship_4(self):
        if self.ships == 0:
            x = np.random.randint(10)
            y = np.random.randint(10)
        else:
            y = ord(input("First coordinate(A-J): ").lower())-97
            x = int(input("Second coordinate(1-10): "))-1
        z = self.rand_orient_4(x,y)
        if z == 'N':
            self.board[(x,x-1,x-2,x-3),(y)] = "4"
            self.inv += [(x,y), (x-1,y), (x-2,y), (x-3,y)]
        elif z == 'S':
            self.board[(x,x+1,x+2,x+3),(y)] = "4"
            self.inv += [(x,y), (x+1,y), (x+2,y), (x+3,y)]
        elif z == 'E':
            self.board[(x),(y,y+1,y+2,y+3)] = "4"
            self.inv += [(x,y), (x,y+1), (x,y+2), (x,y+3)]
        elif z == 'W':
            self.board[(x),(y,y-1,y-2,y-3)] = "4"
            self.inv += [(x,y), (x,y-1), (x,y-2), (x,y-3)]
        if self.ships == 1:
            print(self.board)

    def check_items(self,items,lst):
        for i in lst:
            for j in items:
                if i == j:
                    return(1)
        return(0)

    def rand_coord(self):
        while True:
            if self.ships == 0:
                x = np.random.randint(10)
                y = np.random.randint(10)
            else:
                try:
                    y = ord(input("First coordinate(A-J): ").lower())-97
                    x = int(input("Second coordinate(1-10): "))-1
                except:
                    print("Invalid coordinate")
                    continue
            #inner board
            if 0 not in [x,y] and 9 not in [x,y]:
                if self.check_items([self.board[x,y], self.board[x-1,y],self.board[x+1,y],\
                self.board[x,y+1],self.board[x,y-1],self.board[x-1,y-1],self.board[x+1,y+1],\
                self.board[x-1,y+1],self.board[x+1,y-1]], self.items) == 0:
                    break
            #top board
            elif x == 0:
                if y != 9 and y != 0:
                    if self.check_items([self.board[x,y],self.board[x+1,y],self.board[x,y+1],\
                    self.board[x,y-1],self.board[x+1,y+1],self.board[x+1,y-1]], self.items) == 0:
                        break
                #top-left corner
                elif y == 0:
                    if self.check_items([self.board[x,y],self.board[x+1,y],self.board[x,y+1],self.board[x+1,y+1]], self.items) == 0:
                        break
                #top-right corner
                elif y == 9:
                    if self.check_items([self.board[x,y],self.board[x+1,y],self.board[x,y-1],self.board[x+1,y-1]], self.items) == 0:
                        break
            #bottom board
            elif x == 9:
                if y != 9 and y != 0:
                    if self.check_items([self.board[x,y], self.board[x-1,y],self.board[x,y+1],\
                    self.board[x,y-1],self.board[x-1,y-1],self.board[x-1,y+1]], self.items) == 0:
                        break
                #bottom-right corner
                elif y == 0:
                    if self.check_items([self.board[x,y],self.board[x-1,y],self.board[x,y+1],self.board[x-1,y+1]], self.items) == 0:
                        break
                #bottom-left corner
                elif y == 9:
                    if self.check_items([self.board[x,y],self.board[x-1,y],self.board[x,y-1],self.board[x-1,y-1]], self.items) == 0:
                        break
            #left board
            elif y == 0:
                if x != 9 and x != 0:
                    if self.check_items([self.board[x,y], self.board[x-1,y],self.board[x+1,y],\
                    self.board[x,y+1],self.board[x+1,y+1],self.board[x-1,y+1]], self.items) == 0:
                        break
            #right board
            elif y == 9:
                if x != 9 and x != 0:
                    if self.check_items([self.board[x,y], self.board[x-1,y],self.board[x+1,y],\
                    self.board[x,y-1],self.board[x-1,y-1],self.board[x+1,y-1]], self.items) == 0:
                        break
            if self.ships == 1:
                print("Invalid coordinates, remember: the ships cannot overlap.")
        return(x,y)

    def rand_orient_2(self,x,y):
        while True:
            if self.ships == 0:
                z = np.random.choice(['N','S','E','W'])
            else:
                z = input("Orient(N,S,E,W): ").upper()
            #board limit
            if z == 'N':
                #top board
                if x-1 == 0:
                    break
                elif x-1 > 0 and self.board[x-2,y] not in self.items:
                    #inner board
                    if y != 9 and y != 0:
                        if self.check_items([self.board[x-2,y-1],self.board[x-2,y+1]], self.items) == 0:
                            break
                    #right board
                    elif y == 9:
                        if self.board[x-2,y-1] not in self.items:
                            break
                    #left board
                    elif y == 0:
                        if self.board[x-2,y+1] not in self.items:
                            break
            #board limit
            elif z == 'S':
                #bottom board
                if x+1 == 9:
                    break
                elif x+1 < 9 and self.board[x+2,y] not in self.items:
                    #inner board
                    if y != 9 and y != 0:
                        if self.check_items([self.board[x+2,y-1],self.board[x+2,y+1]], self.items) == 0:
                            break
                    #right board
                    elif y == 9:
                        if self.board[x+2,y-1] not in self.items:
                            break
                    #left board
                    elif y == 0:
                        if self.board[x+2,y+1] not in self.items:
                            break
            #board limit
            elif z == 'E':
                #right board
                if y+1 == 9:
                    break
                elif y+1 < 9 and self.board[x,y+2] not in self.items:
                    #inner board
                    if x != 9 and x != 0:
                        if self.check_items([self.board[x-1,y+2],self.board[x+1,y+2]], self.items) == 0:
                            break
                    #bottom board
                    elif x == 9:
                        if self.board[x-1,y+2] not in self.items:
                            break
                    #top board
                    elif x == 0:
                        if self.board[x+1,y+2] not in self.items:
                            break
            #board limit
            elif z == 'W':
                #left board
                if y-1 == 0:
                    break
                elif y-1 > 0 and  self.board[x,y-2] not in self.items:
                    #inner board
                    if x != 9 and x != 0:
                        if self.check_items([self.board[x-1,y-2],self.board[x+1,y-2]], self.items) == 0:
                            break
                    #bottom board
                    elif x == 9:
                        if self.board[x-1,y-2] not in self.items:
                            break
                    #top board
                    elif x == 0:
                        if self.board[x+1,y-2] not in self.items:
                            break
            if self.ships == 1:
                print("Invalid orientation, remember: the ships cannot overlap.")
        return(z)

    def rand_orient_3(self,x,y):
        while True:
            if self.ships == 0:
                z = np.random.choice(['N','S','E','W'])
            else:
                z = input("Orient(N,S,E,W): ").upper()

            if z == 'N':
                #top board
                if  x-2 == 0 and self.board[x-2,y] not in self.items:
                    if y != 9 and y != 0:
                        if self.check_items([self.board[x-2,y-1],self.board[x-2,y+1]], self.items) == 0:
                            break
                    #top-right corner
                    if y == 9:
                        if self.board[x-2,y-1] not in self.items:
                            break
                    #top-left corner
                    elif y == 0:
                        if self.board[x-2,y+1] not in self.items:
                            break
                #inner board
                elif  x-2 > 0 and self.check_items([self.board[x-3,y],self.board[x-2,y]], self.items) == 0:
                    if y != 9 and y != 0:
                        if self.check_items([self.board[x-2,y-1],self.board[x-2,y+1]], self.items) == 0:
                            if self.check_items([self.board[x-3,y-1],self.board[x-3,y+1]], self.items) == 0:
                                break
                        #right board
                        elif y == 9:
                            if self.board[x-2,y-1] not in self.items:
                                break
                        #left board
                        elif y == 0:
                            if self.board[x-2,y+1] not in self.items:
                                break
            #board limit
            elif z == 'S':
                #bottom board
                if  x+2 == 9 and self.board[x+2,y] not in self.items:
                    if y != 9 and y != 0:
                        if self.check_items([self.board[x+2,y-1],self.board[x+2,y+1]], self.items) == 0:
                            break
                    #bottom-right corner
                    elif y == 9:
                        if self.board[x+2,y-1] not in self.items:
                            break
                    #bottom-left corner
                    elif y == 0:
                        if self.board[x+2,y+1] not in self.items:
                            break
                #inner board
                elif  x+2 < 9 and self.check_items([self.board[x+3,y],self.board[x+2,y]], self.items) == 0:
                    if y != 9 and y != 0:
                        if self.check_items([self.board[x+3,y-1],self.board[x+3,y+1]], self.items) == 0:
                            break
                    #right board
                    elif y == 9:
                        if self.board[x+3,y-1] not in self.items:
                            break
                    #left board
                    elif y == 0:
                        if self.board[x+3,y+1] not in self.items:
                            break
            #board limit
            elif z == 'E':
                #right board
                if y+2 == 9 and self.board[x,y+2] not in self.items:
                    if x != 9 and x != 0:
                        if self.check_items([self.board[x-1,y+2],self.board[x+1,y+2]], self.items) == 0:
                            break
                    #bottom-right corner
                    elif x == 9:
                        if self.board[x-1,y+2] not in self.items:
                            break
                    #top-right corner
                    elif x == 0:
                        if self.board[x+1,y+2] not in self.items:
                            break
                #inner board
                elif  y+2 < 9 and self.check_items([self.board[x,y+2],self.board[x,y+3]], self.items) == 0:
                    if x != 9 and x != 0:
                        if self.check_items([self.board[x-1,y+3],self.board[x+1,y+3]], self.items) == 0:
                            break
                    #bottom board
                    elif x == 9:
                        if self.board[x-1,y+3] not in self.items:
                            break
                    #top board
                    elif x == 0:
                        if self.board[x+1,y+3] not in self.items:
                            break
            #board limit
            elif z == 'W':
                #left board
                if  y-2 == 0 and self.board[x,y-2] not in self.items:
                    if x != 9 and x != 0:
                        if self.check_items([self.board[x-1,y-2],self.board[x+1,y-2]], self.items) == 0:
                            break
                    #bottom-left corner
                    elif x == 9:
                        if self.board[x-1,y-2] not in self.items:
                            break
                    #top-left corner
                    elif x == 0:
                        if self.board[x+1,y-2] not in self.items:
                            break
                #inner board
                elif y-2 > 0 and self.board[x,y-3] not in self.items and self.board[x,y-2] not in self.items:
                    if x != 9 and x != 0:
                        if self.check_items([self.board[x-1,y-3],self.board[x+1,y-3]], self.items) == 0:
                            break
                    #bottom board
                    elif x == 9:
                        if self.board[x-1,y-3] not in self.items:
                            break
                    #top board
                    elif x == 0:
                        if self.board[x+1,y-3] not in self.items:
                            break
            if self.ships == 1:
                print("Invalid orientation, remember: the ships cannot overlap.")
        return(z)

    def rand_orient_4(self,x,y):
        while True:
            if self.ships == 0:
                z = np.random.choice(['N','S','E','W'])
            else:
                z = input("Orient(N,S,E,W): ").upper()
            #board limits
            if (z == 'N' and x-3 >= 0):
                break
            elif (z == 'S' and x+3 <= 9):
                break
            elif (z == 'E' and y+3 <= 9):
                break
            elif (z == 'W' and y-3 >= 0):
                break
            if self.ships == 1:
                print("Invalid orientation, out of board limits.")
        return(z)

    def set_border(self,x,y):
        #inner board
        if 0 not in [x,y] and 9 not in [x,y]:
            self.board[(x+1),(y-1,y+1)] = "W"
            self.board[(x-1),(y-1,y+1)] = "W"
            self.board_machine[(x+1),(y-1,y+1)] = "W"
            self.board_machine[(x-1),(y-1,y+1)] = "W"
        #top board
        elif x == 0:
            if y != 9 and y != 0:
                self.board[(x+1),(y+1,y-1)] = 'W'
                self.board_machine[(x+1),(y+1,y-1)] = 'W'
            #top-left corner
            elif y == 0:
                self.board[x+1,y+1] = 'W'
                self.board_machine[x+1,y+1] = 'W'
            #top-right corner
            elif y == 9:
                self.board[x+1,y-1] = 'W'
                self.board_machine[x+1,y-1] = 'W'
        #bottom board
        elif x == 9:
            if y != 9 and y != 0:
                self.board[(x-1),(y-1,y+1)] = 'W'
                self.board_machine[(x-1),(y-1,y+1)] = 'W'
            #bottom-right corner
            elif y == 0:
                self.board[x-1,y+1] = 'W'
                self.board_machine[x-1,y+1] = 'W'
            #bottom-left corner
            elif y == 9:
                self.board[x-1,y-1] = 'W'
                self.board_machine[x-1,y-1] = 'W'
        #left board
        elif y == 0:
            if x != 9 and x != 0:
                self.board[(x+1,x-1),(y+1)] = 'W'
                self.board_machine[(x+1,x-1),(y+1)] = 'W'
        #right board
        elif y == 9:
            if x != 9 and x != 0:
                self.board[(x-1,x+1),(y-1)] = 'W'
                self.board_machine[(x-1,x+1),(y-1)] = 'W'
