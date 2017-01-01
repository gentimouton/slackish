import random
import string


class NPC():
    def __init__(self, logic, title, name, is_human):
        self.logic = logic
        self.title = title
        self.name = name
        self.is_human = is_human
        self.rooms = {}
    
    def join_room(self, room):
        self.rooms[room.name] = room
        
    def update(self, tick):
        if not self.is_human:
            # display a random message every tick
            txt = ''.join([random.choice(string.ascii_lowercase + string.digits) 
                           for _ in range(12)])
            for room in self.rooms.values():
                room.post_msg(txt, self) 