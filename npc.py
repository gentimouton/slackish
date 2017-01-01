import random
import string


class NPC():
    def __init__(self, logic, title, name):
        self.logic = logic
        self.title = title
        self.name = name
        self.rooms = {}
    
    def join_room(self, room):
        self.rooms[room.name] = room
        
    def update(self):
        # display a random message every tick
        txt = ''.join([random.choice(string.ascii_lowercase + string.digits) 
                       for _ in range(12)])
        for room in self.rooms.values():
            room.post_msg(txt, self) 