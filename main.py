import classes as cl
import functions as func

func.welcome()
difficulty = func.difficulty()
player = cl.Board(1)
machine = cl.Board(2)

while True:
    func.player_fire(player)
    func.machine_fire(machine, difficulty)
    if func.options(player, machine) == 1:
        break






