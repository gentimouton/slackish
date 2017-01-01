import random

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
        # create rooms
        self.rooms = {}
        self.rooms['execs'] = Room(self, 'execs')
        # create NPCs
        self.npcs = {}  # indexed by title
        for title, name in NAMES.items():
            self.npcs[title] = NPC(self, title, name)
        
    def start(self, gui):
        self.gui = gui
        exec_titles = ['CEO', 'CTO']
        for title in exec_titles:
            exec_npc = self.npcs[title]
            exec_npc.join_room(self.rooms['execs'])
        
        
    def stop(self):
        self.game_over = True

    def i_say(self, txt):
        if txt != '':
            self.i_say_queue.append(txt)

        
        
    def update(self):
        # process player messages right away
        while self.i_say_queue:
            txt = self.i_say_queue.pop()
            self.gui.show_msg(txt, NAMES[MY_TITLE], MY_TITLE)
            if txt == 'exit':
                self.game_over = True
        
        for npc in self.npcs.values():
            npc.update()
        for room in self.rooms.values():
            room.update()
    
    
    
    
    # getter
    def get_stats(self, title=MY_TITLE):
        return {
            'title': title,
            'name': NAMES[title]            
            }
    
    # NPC manager
    # TODO: NPCs should have access to posting to the chatrooms they belong to.    
    def say(self, text, name, title):
        self.gui.show_msg(text, name, title)
        