from gui import GUI
from logic import Logic


def run():
    logic = Logic()
    gui = GUI(logic)
    logic.gui = gui
    
    logic.start()
    while not logic.game_over:
        logic.update()
        gui.update()
    gui.kill()

if __name__ == '__main__':
    run()
    