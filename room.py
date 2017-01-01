
class Room():
    
    def __init__(self, logic, name):
        self.logic = logic
        self.name = name
        self.members = {} # maps name to NPC
        self.chat_history = []
        self.msg_queue = []
        
    def enjoin_member(self, npc):
        self.members[npc.name] = npc
        
    def post_msg(self, txt, npc):
        msg_dict = {'txt': txt, 'npc': npc}
        self.msg_queue.append(msg_dict)
        
    def update(self, tick):
        for msg in self.msg_queue:
            txt = msg['txt']
            name = msg['npc'].name
            title = msg['npc'].title
            self.logic.gui.show_msg(txt, name, title)
            self.chat_history.append(msg)
            self.msg_queue = []
            