import random
import time

from npc import NPC
from room import Room


SEED = 1
NAMES = {
    'CEO': 'John',
    'CTO': 'Mary'
    }
MY_TITLE = 'CTO'
random.seed(SEED)


class Logic():
    def __init__(self):
        self.gui = None # set at Logic.start()
        self.game_over = False
        self.i_say_queue = []
        self.last_npc_tick = None
        self.tick = 0
        # create rooms
        self.rooms = {}
        self.rooms['execs'] = Room(self, 'execs')
        # create NPCs
        self.npcs = {}  # indexed by title
        for title, name in NAMES.items():
            is_human = title == MY_TITLE
            self.npcs[title] = NPC(self, title, name, is_human)
        
    def start(self, gui):
        self.gui = gui
        exec_titles = ['CEO', 'CTO']
        for title in exec_titles:
            exec_npc = self.npcs[title]
            exec_npc.join_room(self.rooms['execs'])
        self.last_npc_tick = time.time()
        
        
    def stop(self):
        self.game_over = True
        
    def i_say(self, txt):
        if txt != '':
            self.i_say_queue.append(txt)

        
        
    def update(self):
        # process player messages ASAP
        while self.i_say_queue:
            txt = self.i_say_queue.pop()
            self.gui.show_msg(txt, NAMES[MY_TITLE], MY_TITLE)
            if txt == 'exit':
                self.game_over = True
        # update NPCs every X seconds
        now = time.time()
        if now - self.last_npc_tick >= 1:
            for npc in self.npcs.values():
                npc.update(self.tick)
            self.last_npc_tick = now
            self.tick += 1
        # update rooms ASAP
        for room in self.rooms.values():
            room.update(self.tick)
        
        
        
    # getter
    def get_stats(self, title=MY_TITLE):
        return {
            'title': title,
            'name': NAMES[title]            
            }
            