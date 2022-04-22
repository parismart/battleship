import numpy as np

class Board():

    def __init__(self,id):
        self.id = id
        self.board = np.full((10,10)," ")
        self.board_machine = np.full((10,10)," ")
        self.inv = []
        self.ships = []
        self.coords_free()
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

    def coords_free(self):
        for i in range(10):
            for j in range(10):
                self.ships.append((i,j))

    def set_ships(self):
        self.set_ship_4()
        self.set_ships_3()
        self.set_ships_2()
        self.set_ships_1()

    def set_ships_1(self):
        #Asigna aleatoriamente 4 barcos de eslora 1
        for i in range(4):
            while True:
                x = np.random.randint(10)
                y = np.random.randint(10)
                #Comprueba limites del tablero
                if 0 not in [x,y] and 9 not in [x,y]:
                    #Comprueba alrrededores de la coordenada aleatoria
                    if 'O' not in [self.board[x,y], self.board[x-1,y],self.board[x+1,y],\
                    self.board[x,y+1],self.board[x,y-1],self.board[x-1,y-1],self.board[x+1,y+1],\
                    self.board[x-1,y+1],self.board[x+1,y-1]]:
                        break
            #Establecer barco
            self.board[x,y] = "O"
            self.inv += [(x,y)]
        return(self.board)

    def set_ships_2(self):
       #Asigna aleatoriamente 3 barco de eslora 2
        for i in range(3):
            while True:
                x = np.random.randint(10)
                y = np.random.randint(10)
                #Comprueba alrrededores de la coordenada aleatoria
                if 0 not in [x,y] and 9 not in [x,y]:
                    if 'O' not in [self.board[x,y], self.board[x-1,y],self.board[x+1,y],self.board[x,y+1],\
                    self.board[x,y-1],self.board[x-1,y-1],self.board[x+1,y+1],\
                    self.board[x-1,y+1],self.board[x+1,y-1]]:
                        break
            while True:
                z = np.random.choice(['N','S','E','W'])
                #Comprueba limites del tablero y barcos alrrededor
                if (z == 'N' and x-1 >= 0):
                    if x-1 == 0:
                        break
                    elif 'O' not in [self.board[x-2,y],self.board[x-2,y+1],self.board[x-2,y-1]]:
                        break
                elif (z == 'S' and x+1 <= 9):
                    if x+1 == 9:
                        break
                    elif 'O' not in [self.board[x+2,y],self.board[x-2,y+1],self.board[x-2,y-1]]:
                        break
                elif (z == 'E' and y+1 <= 9):
                    if y+1 == 9:
                        break
                    elif 'O' not in [self.board[x,y+2],self.board[x+1,y+2],self.board[x-1,y+2]]:
                        break
                elif (z == 'W' and y-1 >= 0):
                    if y-1 == 0:
                        break
                    elif 'O' not in [self.board[x,y-2],self.board[x+1,y-2],self.board[x-1,y-2]]:
                        break
            #Establecer barcos
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
        return(self.board)

    def set_ships_3(self):
       #Asigna aleatoriamente 2 barco de eslora 3
        for i in range(2):
            while True:
                x = np.random.randint(10)
                y = np.random.randint(10)
                #Comprueba alrrededores de la coordenada aleatoria
                if 0 not in [x,y] and 9 not in [x,y]:
                    if 'O' not in [self.board[x,y], self.board[x-1,y],self.board[x+1,y],self.board[x,y+1],\
                    self.board[x,y-1],self.board[x-1,y-1],self.board[x+1,y+1],\
                    self.board[x-1,y+1],self.board[x+1,y-1]]:
                        break
            while True:
                z = np.random.choice(['N','S','E','W'])
                #Comprueba limites del tablero y barcos alrrededor
                if (z == 'N' and x-2 >= 0):
                    if 'O' not in [self.board[x-2,y],self.board[x-2,y+1],self.board[x-2,y-1]]:
                        if x-2 == 0:
                            break
                        elif 'O' not in [self.board[x-3,y],self.board[x-3,y+1],self.board[x-3,y-1]]:
                            break
                elif (z == 'S' and x+2 <= 9):
                    if 'O' not in [self.board[x+2,y],self.board[x+2,y+1],self.board[x+2,y-1]]:
                        if x+2 == 9:
                            break
                        elif 'O' not in [self.board[x+3,y],self.board[x+3,y+1],self.board[x+3,y-1]]:
                            break
                elif (z == 'E' and y+2 <= 9):
                    if 'O' not in [self.board[x,y+2],self.board[x+1,y+2],self.board[x-1,y+2]]:
                        if y+2 == 9:
                            break
                        elif 'O' not in [self.board[x,y+3],self.board[x+1,y+3],self.board[x-1,y+3]]:
                            break
                elif (z == 'W' and y-2 >= 0):
                    if 'O' not in [self.board[x,y-2],self.board[x+1,y-2],self.board[x-1,y-2]]:
                        if y-2 == 0:
                            break
                        elif 'O' not in [self.board[x,y-3],self.board[x+1,y-3],self.board[x-1,y-3]]:
                            break
            #Establecer barcos
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
        return(self.board)


    def set_ship_4(self):
        #Asigna aleatoriamente 1 barco de eslora 4
        x = np.random.randint(10)
        y = np.random.randint(10)
        while True:
            z = np.random.choice(['N','S','E','W'])
            #Comprueba que la orientación sea correcta y no se salga del tablero
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
        #Establecer barco
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
        return(self.board)
