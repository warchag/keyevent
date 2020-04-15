import tkinter as tk
import pygubu
from tkinter import ttk
class Gui():
    def __init__(self):
        self.builder = builder = pygubu.Builder()
        builder.add_from_file(r'C:\Users\nara-\Desktop\KeyboardEventtoUse\KeyboardEventtoUse\x.ui')
        self.mainwindows = builder.get_object('Frame_1')
        
    def Draw_Gui(self):
        self.mainwindows.mainloop()
