import movie_manager as mml

def main():
    mm = {}
    while True:
        line = input()
        
        commands = input.split(" ")

        if commands[0] == "RR":
            commandRR(commands, mm)
        elif commands[0] == "RA":
            commandRA(commands, mm)
        elif commands[0] == "RF":
            commandRF(commands, mm)

def commandRR(commands, mm):
    name = commands[1]
    if mml.has_director(mm, name):
        print("Realizador existente.")
    else:
        mml.add_director(mm, name)
        print("Realizador registado com sucesso.")
 
def commandRA(commands, mm):
    name = commands[1]
    if mml.has_actor(mm, name):
        print("Ator existente.")
    else:
        mml.add_ator(mm, name)
        print("Ator registado com sucesso.")

def commandRF(comamnds, mm):
    pass

if __name__ == "__main__":
    main()