import numpy as np
import functions as func

class Board():

    def __init__(self,place=0):
        self.board = np.full((12,12)," ")
        self.board_machine = np.full((12,12)," ")
        self.items = ["1","2","3","4","5","6","8"]
        self.ships = {"Carrier":4,"Bat_1":3,"Bat_2":3,"Dest_1":2,"Dest_2":2,"Dest_3":2}
        self.borders = {"Carrier":[],"Bat_1":[],"Bat_2":[],"Dest_1":[],"Dest_2":[],"Dest_3":[]}
        self.inv = []
        self.place = place
        self.set_ships()
        self.axis()

    def axis(self):
        for i in range(1,11):
            self.board[0][i] = func.num_letter(i)
            self.board[11][i] = func.num_letter(i)
            self.board[i][0] = i-1
            self.board[i][11] = i-1
            self.board_machine[0][i] = func.num_letter(i)
            self.board_machine[11][i] = func.num_letter(i)
            self.board_machine[i][0] = i-1
            self.board_machine[i][11] = i-1

    def fire(self,x, y):
        if (x, y) not in self.inv:
            self.board_machine[x, y] = 'W'
            self.board[x, y] = 'W'
            print(color.blue + "Water" + color.reset)
            return(0)
        else:
            print("Match")
            self.check_sunk(x,y)
            self.set_border(x, y)
            self.board_machine[x, y] = 'X'
            self.board[x, y] = 'X'
            self.inv.remove((x, y))
            return(1)

    def check_sunk(self,x,y):
        if self.board[x,y] == '1':
            print("Sunken Patrol Boat")
        elif self.board[x,y] == '2':
            self.ships["Dest_1"] -= 1
            if self.ships["Dest_1"] == 0:
                print("Sunken Destroyer")
                self.board[self.borders["Dest_1"]] = "W"
                self.board_machine[self.borders["Dest_1"]] = "W"
        elif self.board[x,y] == '5':
            self.ships["Dest_2"] -= 1
            if self.ships["Dest_2"] == 0:
                print("Sunken Destroyer")
                self.board[self.borders["Dest_2"]] = "W"
                self.board_machine[self.borders["Dest_2"]] = "W"
        elif self.board[x,y] == '8':
            self.ships["Dest_3"] -= 1
            if self.ships["Dest_3"] == 0:
                print("Sunken Destroyer")
                self.board[self.borders["Dest_3"]] = "W"
                self.board_machine[self.borders["Dest_2"]] = "W"
        elif self.board[x,y] == '3':
            self.ships["Bat_1"] -= 1
            if self.ships["Bat_1"] == 0:
                print("Sunken Battleship")
                self.board[self.borders["Bat_1"]] = "W"
                self.board_machine[self.borders["Bat_1"]] = "W"
        elif self.board[x,y] == '6':
            self.ships["Bat_2"] -= 1
            if self.ships["Bat_2"] == 0:
                print("Sunken Battleship")
                self.board[self.borders["Bat_2"]] = "W"
                self.board_machine[self.borders["Bat_1"]] = "W"
        elif self.board[x,y] == '4':
            self.ships["Carrier"] -= 1
            if self.ships["Carrier"] == 0:
                print("Sunken Carrier")
                self.board[self.borders["Carrier"]] = "W"
                self.board_machine[self.borders["Carrier"]] = "W"

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
            if self.place == 1:
                print(self.board)

    def set_ships_2(self):
        n = -1
        for i in range(3):
            n += 3
            x, y = self.rand_coord()
            z = self.rand_orient_2(x,y)
            if z == 'N':
                self.board[(x,x-1),(y)] = str(n)
                self.inv += [(x,y), (x-1,y)]
                if i == 0:
                    self.borders["Dest_1"] = (x+1,x-2),(y)
                elif i == 1:
                    self.borders["Dest_2"] = (x+1,x-2),(y)
                else:
                    self.borders["Dest_3"] = (x+1,x-2),(y)
            elif z == 'S':
                self.board[(x,x+1),(y)] = str(n)
                self.inv += [(x,y), (x+1,y)]
                if i == 0:
                    self.borders["Dest_1"] = (x-1,x+2),(y)
                elif i == 1:
                    self.borders["Dest_2"] = (x-1,x+2),(y)
                else:
                    self.borders["Dest_3"] = (x-1,x+2),(y)
            elif z == 'E':
                self.board[(x),(y,y+1)] = str(n)
                self.inv += [(x,y), (x,y+1)]
                if i == 0:
                    self.borders["Dest_1"] = (x),(y-1,y+2)
                elif i == 1:
                    self.borders["Dest_2"] = (x),(y-1,y+2)
                else:
                    self.borders["Dest_3"] = (x),(y-1,y+2)
            elif z == 'W':
                self.board[(x),(y,y-1)] = str(n)
                self.inv += [(x,y), (x,y-1)]
                if i == 0:
                    self.borders["Dest_1"] = (x),(y+1,y-2)
                elif i == 1:
                    self.borders["Dest_2"] = (x),(y+1,y-2)
                else:
                    self.borders["Dest_3"] = (x),(y+1,y-2)
            if self.place == 1:
                print(self.board)

    def set_ships_3(self):
        n = 0
        for i in range(2):
            n += 3
            x, y = self.rand_coord()
            z = self.rand_orient_3(x,y)
            if z == 'N':
                self.board[(x,x-1,x-2),(y)] = str(n)
                self.inv += [(x,y), (x-1,y), (x-2,y)]
                if i == 0:
                    self.borders["Bat_1"] = (x+1,x-3),(y)
                else:
                    self.borders["Bat_2"] = (x+1,x-3),(y)
            elif z == 'S':
                self.board[(x,x+1,x+2),(y)] = str(n)
                self.inv += [(x,y), (x+1,y), (x+2,y)]
                if i == 0:
                    self.borders["Bat_1"] = (x-1,x+3),(y)
                else:
                    self.borders["Bat_2"] = (x-1,x+3),(y)
            elif z == 'E':
                self.board[(x),(y,y+1,y+2)] = str(n)
                self.inv += [(x,y), (x,y+1), (x,y+2)]
                if i == 0:
                    self.borders["Bat_1"] = (x),(y-1,y+3)
                else:
                    self.borders["Bat_2"] = (x),(y-1,y+3)
            elif z == 'W':
                self.board[(x),(y,y-1,y-2)] = str(n)
                self.inv += [(x,y), (x,y-1), (x,y-2)]
                if i == 0:
                    self.borders["Bat_1"] = (x),(y+1,y-3)
                else:
                    self.borders["Bat_2"] = (x),(y+1,y-3)
            if self.place == 1:
                print(self.board)

    def set_ship_4(self):
        if self.place == 0:
            x = np.random.randint(1,11)
            y = np.random.randint(1,11)
        else:
            y = ord(input("First coordinate(A-J): ").lower())-107
            x = int(input("Second coordinate(1-10): "))-1
        z = self.rand_orient_4(x,y)
        if z == 'N':
            self.board[(x,x-1,x-2,x-3),(y)] = "4"
            self.inv += [(x,y), (x-1,y), (x-2,y), (x-3,y)]
            self.borders["Carrier"] = (x+1,x-4),(y)
        elif z == 'S':
            self.board[(x,x+1,x+2,x+3),(y)] = "4"
            self.inv += [(x,y), (x+1,y), (x+2,y), (x+3,y)]
            self.borders["Carrier"] = (x+4,x-1),(y)
        elif z == 'E':
            self.board[(x),(y,y+1,y+2,y+3)] = "4"
            self.inv += [(x,y), (x,y+1), (x,y+2), (x,y+3)]
            self.borders["Carrier"] = (x),(y-1,y+4)
        elif z == 'W':
            self.board[(x),(y,y-1,y-2,y-3)] = "4"
            self.inv += [(x,y), (x,y-1), (x,y-2), (x,y-3)]
            self.borders["Carrier"] = (x),(y+1,y-4)
        if self.place == 1:
            print(self.board)

    def check_items(self,items,lst):
        for i in lst:
            for j in items:
                if i == j:
                    return(1)
        return(0)

    def rand_coord(self):
        while True:
            if self.place == 0:
                x = np.random.randint(1,11)
                y = np.random.randint(1,11)
            else:
                try:
                    y = ord(input("First coordinate(A-J): ").lower())-107
                    x = int(input("Second coordinate(1-10): "))-1
                except:
                    print("Invalid coordinate")
                    continue
            #inner board
            if 1 not in [x,y] and 10 not in [x,y]:
                if self.check_items([self.board[x,y], self.board[x-1,y],self.board[x+1,y],\
                self.board[x,y+1],self.board[x,y-1],self.board[x-1,y-1],self.board[x+1,y+1],\
                self.board[x-1,y+1],self.board[x+1,y-1]], self.items) == 0:
                    break
            #top board
            elif x == 1:
                if y != 10 and y != 1:
                    if self.check_items([self.board[x,y],self.board[x+1,y],self.board[x,y+1],\
                    self.board[x,y-1],self.board[x+1,y+1],self.board[x+1,y-1]], self.items) == 0:
                        break
                #top-left corner
                elif y == 1:
                    if self.check_items([self.board[x,y],self.board[x+1,y],self.board[x,y+1],self.board[x+1,y+1]], self.items) == 0:
                        break
                #top-right corner
                elif y == 10:
                    if self.check_items([self.board[x,y],self.board[x+1,y],self.board[x,y-1],self.board[x+1,y-1]], self.items) == 0:
                        break
            #bottom board
            elif x == 10:
                if y != 10 and y != 1:
                    if self.check_items([self.board[x,y], self.board[x-1,y],self.board[x,y+1],\
                    self.board[x,y-1],self.board[x-1,y-1],self.board[x-1,y+1]], self.items) == 0:
                        break
                #bottom-right corner
                elif y == 1:
                    if self.check_items([self.board[x,y],self.board[x-1,y],self.board[x,y+1],self.board[x-1,y+1]], self.items) == 0:
                        break
                #bottom-left corner
                elif y == 10:
                    if self.check_items([self.board[x,y],self.board[x-1,y],self.board[x,y-1],self.board[x-1,y-1]], self.items) == 0:
                        break
            #left board
            elif y == 1:
                if x != 10 and x != 1:
                    if self.check_items([self.board[x,y], self.board[x-1,y],self.board[x+1,y],\
                    self.board[x,y+1],self.board[x+1,y+1],self.board[x-1,y+1]], self.items) == 0:
                        break
            #right board
            elif y == 10:
                if x != 10 and x != 1:
                    if self.check_items([self.board[x,y], self.board[x-1,y],self.board[x+1,y],\
                    self.board[x,y-1],self.board[x-1,y-1],self.board[x+1,y-1]], self.items) == 0:
                        break
            if self.place == 1:
                print("Invalid coordinates, remember: the ships cannot overlap.")
        return(x,y)

    def rand_orient_2(self,x,y):
        while True:
            if self.place == 0:
                z = np.random.choice(['N','S','E','W'])
            else:
                z = input("Orient(N,S,E,W): ").upper()
            #board limit
            if z == 'N':
                #top board
                if x-1 == 1:
                    break
                elif x-1 > 1 and self.board[x-2,y] not in self.items:
                    #inner board
                    if y != 10 and y != 1:
                        if self.check_items([self.board[x-2,y-1],self.board[x-2,y+1]], self.items) == 0:
                            break
                    #right board
                    elif y == 10:
                        if self.board[x-2,y-1] not in self.items:
                            break
                    #left board
                    elif y == 1:
                        if self.board[x-2,y+1] not in self.items:
                            break
            #board limit
            elif z == 'S':
                #bottom board
                if x+1 == 10:
                    break
                elif x+1 < 10 and self.board[x+2,y] not in self.items:
                    #inner board
                    if y != 10 and y != 1:
                        if self.check_items([self.board[x+2,y-1],self.board[x+2,y+1]], self.items) == 0:
                            break
                    #right board
                    elif y == 10:
                        if self.board[x+2,y-1] not in self.items:
                            break
                    #left board
                    elif y == 1:
                        if self.board[x+2,y+1] not in self.items:
                            break
            #board limit
            elif z == 'E':
                #right board
                if y+1 == 10:
                    break
                elif y+1 < 10 and self.board[x,y+2] not in self.items:
                    #inner board
                    if x != 10 and x != 1:
                        if self.check_items([self.board[x-1,y+2],self.board[x+1,y+2]], self.items) == 0:
                            break
                    #bottom board
                    elif x == 10:
                        if self.board[x-1,y+2] not in self.items:
                            break
                    #top board
                    elif x == 1:
                        if self.board[x+1,y+2] not in self.items:
                            break
            #board limit
            elif z == 'W':
                #left board
                if y-1 == 1:
                    break
                elif y-1 > 1 and  self.board[x,y-2] not in self.items:
                    #inner board
                    if x != 10 and x != 1:
                        if self.check_items([self.board[x-1,y-2],self.board[x+1,y-2]], self.items) == 0:
                            break
                    #bottom board
                    elif x == 10:
                        if self.board[x-1,y-2] not in self.items:
                            break
                    #top board
                    elif x == 1:
                        if self.board[x+1,y-2] not in self.items:
                            break
            if self.place == 1:
                print("Invalid orientation, remember: the ships cannot overlap.")
        return(z)

    def rand_orient_3(self,x,y):
        while True:
            if self.place == 0:
                z = np.random.choice(['N','S','E','W'])
            else:
                z = input("Orient(N,S,E,W): ").upper()
            if z == 'N':
                #top board
                if  x-2 == 1 and self.board[x-2,y] not in self.items:
                    if y != 10 and y != 1:
                        if self.check_items([self.board[x-2,y-1],self.board[x-2,y+1]], self.items) == 0:
                            break
                    #top-right corner
                    if y == 10:
                        if self.board[x-2,y-1] not in self.items:
                            break
                    #top-left corner
                    elif y == 1:
                        if self.board[x-2,y+1] not in self.items:
                            break
                #inner board
                elif  x-2 > 1 and self.check_items([self.board[x-3,y],self.board[x-2,y]], self.items) == 0:
                    if y != 10 and y != 1:
                        if self.check_items([self.board[x-2,y-1],self.board[x-2,y+1]], self.items) == 0:
                            if self.check_items([self.board[x-3,y-1],self.board[x-3,y+1]], self.items) == 0:
                                break
                        #right board
                        elif y == 10:
                            if self.board[x-2,y-1] not in self.items:
                                break
                        #left board
                        elif y == 1:
                            if self.board[x-2,y+1] not in self.items:
                                break
            #board limit
            elif z == 'S':
                #bottom board
                if  x+2 == 10 and self.board[x+2,y] not in self.items:
                    if y != 10 and y != 1:
                        if self.check_items([self.board[x+2,y-1],self.board[x+2,y+1]], self.items) == 0:
                            break
                    #bottom-right corner
                    elif y == 10:
                        if self.board[x+2,y-1] not in self.items:
                            break
                    #bottom-left corner
                    elif y == 1:
                        if self.board[x+2,y+1] not in self.items:
                            break
                #inner board
                elif  x+2 < 10 and self.check_items([self.board[x+3,y],self.board[x+2,y]], self.items) == 0:
                    if y != 10 and y != 1:
                        if self.check_items([self.board[x+3,y-1],self.board[x+3,y+1]], self.items) == 0:
                            break
                    #right board
                    elif y == 10:
                        if self.board[x+3,y-1] not in self.items:
                            break
                    #left board
                    elif y == 1:
                        if self.board[x+3,y+1] not in self.items:
                            break
            #board limit
            elif z == 'E':
                #right board
                if y+2 == 10 and self.board[x,y+2] not in self.items:
                    if x != 10 and x != 1:
                        if self.check_items([self.board[x-1,y+2],self.board[x+1,y+2]], self.items) == 0:
                            break
                    #bottom-right corner
                    elif x == 10:
                        if self.board[x-1,y+2] not in self.items:
                            break
                    #top-right corner
                    elif x == 1:
                        if self.board[x+1,y+2] not in self.items:
                            break
                #inner board
                elif  y+2 < 10 and self.check_items([self.board[x,y+2],self.board[x,y+3]], self.items) == 0:
                    if x != 10 and x != 1:
                        if self.check_items([self.board[x-1,y+3],self.board[x+1,y+3]], self.items) == 0:
                            break
                    #bottom board
                    elif x == 10:
                        if self.board[x-1,y+3] not in self.items:
                            break
                    #top board
                    elif x == 1:
                        if self.board[x+1,y+3] not in self.items:
                            break
            #board limit
            elif z == 'W':
                #left board
                if  y-2 == 1 and self.board[x,y-2] not in self.items:
                    if x != 10 and x != 1:
                        if self.check_items([self.board[x-1,y-2],self.board[x+1,y-2]], self.items) == 0:
                            break
                    #bottom-left corner
                    elif x == 10:
                        if self.board[x-1,y-2] not in self.items:
                            break
                    #top-left corner
                    elif x == 1:
                        if self.board[x+1,y-2] not in self.items:
                            break
                #inner board
                elif y-2 > 1 and self.board[x,y-3] not in self.items and self.board[x,y-2] not in self.items:
                    if x != 10 and x != 1:
                        if self.check_items([self.board[x-1,y-3],self.board[x+1,y-3]], self.items) == 0:
                            break
                    #bottom board
                    elif x == 10:
                        if self.board[x-1,y-3] not in self.items:
                            break
                    #top board
                    elif x == 1:
                        if self.board[x+1,y-3] not in self.items:
                            break
            if self.place == 1:
                print("Invalid orientation, remember: the ships cannot overlap.")
        return(z)

    def rand_orient_4(self,x,y):
        while True:
            if self.place == 0:
                z = np.random.choice(['N','S','E','W'])
            else:
                z = input("Orient(N,S,E,W): ").upper()
            #board limits
            if (z == 'N' and x-3 >= 1):
                break
            elif (z == 'S' and x+3 <= 10):
                break
            elif (z == 'E' and y+3 <= 10):
                break
            elif (z == 'W' and y-3 >= 1):
                break
            if self.place == 1:
                print("Invalid orientation, out of board limits.")
        return(z)

    def set_border(self,x,y):
        #inner board
        if 1 not in [x,y] and 10 not in [x,y]:
            self.board[(x+1),(y-1,y+1)] = "W"
            self.board[(x-1),(y-1,y+1)] = "W"
            self.board_machine[(x+1),(y-1,y+1)] = "W"
            self.board_machine[(x-1),(y-1,y+1)] = "W"
            if self.board[x,y] == '1':
                self.board[(x),(y-1,y+1)] = "W"
                self.board[(x+1,x-1),(y)] = "W"
                self.board_machine[(x),(y-1,y+1)] = "W"
                self.board_machine[(x+1,x-1),(y)] = "W"

        #top board
        elif x == 1:
            if y != 10 and y != 1:
                self.board[(x+1),(y+1,y-1)] = 'W'
                self.board_machine[(x+1),(y+1,y-1)] = 'W'
                if self.board[x,y] == '1':
                    self.board[(x),(y-1,y+1)] = "W"
                    self.board[(x+1),(y)] = "W"
                    self.board_machine[(x),(y-1,y+1)] = "W"
                    self.board_machine[(x+1),(y)] = "W"
            #top-left corner
            elif y == 1:
                self.board[x+1,y+1] = 'W'
                self.board_machine[x+1,y+1] = 'W'
                if self.board[x,y] == '1':
                    self.board[(x),(y+1)] = "W"
                    self.board[(x+1),(y)] = "W"
                    self.board_machine[(x),(y+1)] = "W"
                    self.board_machine[(x+1),(y)] = "W"
            #top-right corner
            elif y == 10:
                self.board[x+1,y-1] = 'W'
                self.board_machine[x+1,y-1] = 'W'
                if self.board[x,y] == '1':
                    self.board[(x),(y-1)] = "W"
                    self.board[(x+1),(y)] = "W"
                    self.board_machine[(x),(y-10)] = "W"
                    self.board_machine[(x+1),(y)] = "W"
        #bottom board
        elif x == 10:
            if y != 10 and y != 1:
                self.board[(x-1),(y-1,y+1)] = 'W'
                self.board_machine[(x-1),(y-1,y+1)] = 'W'
                if self.board[x,y] == '1':
                    self.board[(x),(y-1,y+1)] = "W"
                    self.board[(x-1),(y)] = "W"
                    self.board_machine[(x),(y-1,y+1)] = "W"
                    self.board_machine[(x-1),(y)] = "W"
            #bottom-right corner
            elif y == 1:
                self.board[x-1,y+1] = 'W'
                self.board_machine[x-1,y+1] = 'W'
                if self.board[x,y] == '1':
                    self.board[(x),(y+1)] = "W"
                    self.board[(x-1),(y)] = "W"
                    self.board_machine[(x),(y+1)] = "W"
                    self.board_machine[(x-1),(y)] = "W"
            #bottom-left corner
            elif y == 10:
                self.board[x-1,y-1] = 'W'
                self.board_machine[x-1,y-1] = 'W'
                if self.board[x,y] == '1':
                    self.board[(x),(y-1)] = "W"
                    self.board[(x-1),(y)] = "W"
                    self.board_machine[(x),(y-1)] = "W"
                    self.board_machine[(x-1),(y)] = "W"
        #left board
        elif y == 1:
            self.board[(x+1,x-1),(y+1)] = 'W'
            self.board_machine[(x+1,x-1),(y+1)] = 'W'
            if self.board[x,y] == '1':
                self.board[(x),(y+1)] = "W"
                self.board[(x-1,x+1),(y)] = "W"
                self.board_machine[(x),(y+1)] = "W"
                self.board_machine[(x-1,x+1),(y)] = "W"
        #right board
        elif y == 10:
            self.board[(x-1,x+1),(y-1)] = 'W'
            self.board_machine[(x-1,x+1),(y-1)] = 'W'
            if self.board[x,y] == '1':
                self.board[(x),(y-1)] = "W"
                self.board[(x-1,x+1),(y)] = "W"
                self.board_machine[(x),(y-1)] = "W"
                self.board_machine[(x-1,x+1),(y)] = "W"

class color:
    green = '\033[92m' #GREEN
    yellow = '\033[93m' #YELLOW
    red = '\033[91m' #RED
    blue = '\033[34m' #BLUE
    cheat = '\033[35m' #CHEAT
    white = '\033[97m' #WHITE
    reset = '\033[0m' #RESET COLOR
