import time

from gui import GUI
from logic import Logic


def run():
    logic = Logic()
    gui = GUI(logic)
    logic.start(gui)
    last_tick = time.time()
    while not logic.game_over:
        now = time.time()
        if now - last_tick >= 2:
            logic.update()
            last_tick = now
        gui.update()
    gui.kill()

if __name__ == '__main__':
    run()
    