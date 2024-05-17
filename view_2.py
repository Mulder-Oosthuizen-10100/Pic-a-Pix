from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk

class SearchFrame(ttk.Frame):

    def __init__(self, master, controller):
        super().__init__(master)

        h = 35
        
        self.controller = controller
        self.edt_search = ttk.Entry(self, font=('JetBrains Mono', 14))
        self.edt_search.pack(side=LEFT, fill=X, expand=True, pady=5, padx=5)

        self.btn_search = ttk.Button(self, text="SEARCH", width=20)
        self.btn_search.pack(side=RIGHT, pady=5, padx=5)

class MainWindow(tk.Tk):

    def __init__(self, controller):
        super().__init__()
        
        self.controller = controller
        self.title('Pick-n-Pix')
        self.geometry('800x600')
        self.iconbitmap('.\\images\\application_icon.ico')
        self.minsize(250,250)

        self.search_frame = SearchFrame(self, controller)
        self.search_frame.pack(side=TOP, pady=(10,5), padx=10, fill=X)

        # self.option_frame = OptionsFrame(self, controller)
        # self.option_frame.pack(side=TOP, pady=(5,10), padx=10, fill=X)

class pnpView2:
    
    def __init__(self, controller) -> None:
        self.root = MainWindow(controller)
        self.root.mainloop()