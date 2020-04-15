import tkinter as tk
from tkinter import ttk
class Gui():
    def __init__(self):
        pass
    def Draw_Gui(self):
        window= tk.Tk()
        window.geometry("500x250")
        window.title("KeyBoard")
        labelTop = tk.Label(window,
                    text = "เลือก Key")
        labelTop.grid(column=0, row=0)
        mykey = []
        for i in range(0,9):
            mykey.append(i)
        cmb = ttk.Combobox(window,values=mykey,state="readonly")
        cmb.grid(column=0, row=1)
        cmb.current(1)
        cmb.bind("<<ComboboxSelected>>", self.callbackFunc)
        window.mainloop()    
    def callbackFunc(self,event):
        print("print ok")                 