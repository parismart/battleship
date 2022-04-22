import classes as cl
import functions as func

func.welcome()
dificulty = func.dificulty()
player = cl.Board(1)
machine = cl.Board(2)

while True:
    func.player_fire(player)
    func.machine_fire(machine, dificulty)
    if func.options(player, machine) == 1:
        break
    #if func.exit_game(player, machine) == 1:
        #break






