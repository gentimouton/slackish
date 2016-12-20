import random
import string
import time

import gui

game_over = False 

my_name =  'John (CEO)'
name_cto = 'Mary (CTO)'
i_say_queue = []
random.seed(1)
last_tick = time.time()
 
 
def i_say(txt):
    if txt != '':
        i_say_queue.append(txt)
    
    
def update():
    
    # process player messages right away
    for txt in i_say_queue:
        gui.show_msg(txt, my_name)
        i_say_queue.pop()
        if txt == 'exit':
            global game_over
            game_over = True
            
    # display a random message every 2 seconds
    now = time.time()
    if now - last_tick > 2:
        txt = ''.join([random.choice(string.ascii_lowercase + string.digits) 
                       for _ in range(12)])
        gui.show_msg(txt, name_cto)
        global last_tick
        last_tick = now 
        
        
def stop():
    global game_over
    game_over = True
