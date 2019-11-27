import movie_manager as mml

def main():
    mm = {}
    while True:
        line = input()
        
        commands = input.split(" ")

        if commands[0] == "RR":
            commandRR(commands, mm)
 
def commandRR(commands, mm):
    name = commands[1]
    if mml.has_director(mm, name):
        print("Realizador existente.")
    else:
        mml.add_director(mm, name)
        print("Realizador registado com sucesso.")

if __name__ == "__main__":
    main()