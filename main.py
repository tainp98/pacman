from app_class import *
import argparse
parse = argparse.ArgumentParser(description="Pacman Game")
parse.add_argument('-s','--select',type=str,required=False ,help='Select A* or BFS')
arg = parse.parse_args()
print(arg.select)
if __name__ == '__main__':
    if arg.select == None:
        app = App()
    else:
        app = App(arg.select)
    app.run()