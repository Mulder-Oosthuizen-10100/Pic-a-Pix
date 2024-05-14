import customtkinter as ctk


class MainWindow(ctk.CTk):

    def __init__(self, controller):
        super().__init__()
        
        self.controller = controller
        self.title('Pick-n-Pix')
        self.geometry('800x600')
        self.iconbitmap('.\\images\\application_icon.ico')

class pnpView:
    
    def __init__(self, controller) -> None:
        self.root = MainWindow(controller)
        self.root.mainloop()
