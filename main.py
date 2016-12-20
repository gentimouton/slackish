"""
Tkinter resources: 
http://zetcode.com/gui/tkinter/introduction/
https://github.com/siddharthasahu/P2P-chat-application
https://docs.python.org/2/library/tkinter.html
http://www.tkdocs.com/tutorial/grid.html
"""

import gui
import logic
  
def run():
    while not logic.game_over:
        logic.update()
        gui.update()
    gui.kill()

if __name__ == '__main__':
    run()
    