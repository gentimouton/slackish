"""
Tkinter resources: 
http://zetcode.com/gui/tkinter/introduction/
https://github.com/siddharthasahu/P2P-chat-application
https://docs.python.org/2/library/tkinter.html
http://www.tkdocs.com/tutorial/grid.html
"""

import Tkinter as tk


class GUI():
    
    def __init__(self, logic):
        self.logic = logic
        root = tk.Tk()  # main window
        root.protocol('WM_DELETE_WINDOW', self.logic.stop)  # cross was clicked
        root.title('Slackish')
        root.resizable(width=False, height=False)
        self.root = root
        self._build_gui()
        
    def _build_gui(self):
        root = self.root
        root.grid()
        
        # top row
        self.label1 = tk.Label(root, text="Rooms").grid(row=0, column=0)
        self.label2 = tk.Label(root, text="Room title").grid(row=0, column=1)
        self.label3 = tk.Label(root, text="Tasks").grid(row=0, column=3)
        
        # mid row
        self.room_list = tk.Listbox(root, width=30)
        self.room_list.grid(row=1, column=0, sticky=tk.NSEW)
         
        self.chat_screen = tk.Text(root, bg="white", width=60, height=20,
                                   state=tk.DISABLED, wrap=tk.WORD)
        self.chat_screen.grid(row=1, column=1)
        chat_scrollbar = tk.Scrollbar(root, command=self.chat_screen.yview,
                                      orient=tk.VERTICAL)
        chat_scrollbar.grid(row=1, column=2, sticky=tk.NS)
        self.chat_screen.config(yscrollcommand=chat_scrollbar.set)
         
        self.task_list = tk.Listbox(root, width=30)
        self.task_list.grid(row=1, column=3, sticky=tk.NS)
        
        # bottom row
        frame = tk.Frame(root)
        frame.grid(column=1, row=2, columnspan=2, sticky=tk.EW)
        name_label = tk.Label(frame, text="TODO: John (CEO):")  # TODO: from logic
        name_label.pack(side=tk.LEFT)
        self.entry = tk.Entry(frame, width=60)
        self.entry.pack(side=tk.LEFT)
        # ways to capture key press: http://stackoverflow.com/a/19148324/856897
        self.entry.bind('<Key>', lambda k: self._on_keypress(k))
        self.entry.focus_set()
        
    def show_msg(self, txt, author, title):
        txtbox = self.chat_screen
        txtbox.config(state=tk.NORMAL)
        txtbox.insert(tk.END, author + ' (' + title + ')' + ': ')
        txtbox.insert(tk.END, txt + '\n')
        txtbox.see(tk.END)
        txtbox.config(state=tk.DISABLED)
    
        
    def _on_keypress(self, key):
        # detect line feed/carriage return
        if key.char in ('\n', '\r') or key.keycode == 2359309: 
            txt = self.entry.get()
            self.entry.delete(0, tk.END)
            self.logic.i_say(txt)
         
    def update(self):
        self.root.update()

    def kill(self):
        self.root.destroy()
