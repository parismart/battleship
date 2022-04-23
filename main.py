import classes as cl
import functions as func

func.welcome()
difficulty = func.difficulty()
player = cl.Board(func.place_ships())
machine = cl.Board()
print(machine.board)

while True:
    func.player_fire(player)
    func.machine_fire(machine, difficulty)
    if func.options(player, machine) == 1:
        break
