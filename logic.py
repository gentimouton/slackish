import random
import string
import time


SEED = 1
NAMES = {
    'CEO': 'John',
    'CTO': 'Mary'
    }
MY_TITLE = 'CEO'

class Logic():
    def __init__(self):
        self.gui = None
        random.seed(SEED)
        self.game_over = False
        self.i_say_queue = []

    def i_say(self,txt):
        if txt != '':
            self.i_say_queue.append(txt)
        
    def update(self):
        # process player messages right away
        for txt in self.i_say_queue:
            self.gui.show_msg(txt, NAMES[MY_TITLE], MY_TITLE)
            
            self.i_say_queue.pop()
            if txt == 'exit':
                self.game_over = True
        # display a random message every second
        now = time.time()
        if now - self.last_tick > 1:
            txt = ''.join([random.choice(string.ascii_lowercase + string.digits) 
                           for _ in range(12)])
            self.gui.show_msg(txt, NAMES['CTO'], 'CTO')
            self.last_tick = now 
    
    def start(self):
        self.last_tick = time.time()
        
    def stop(self):
        self.game_over = True
        