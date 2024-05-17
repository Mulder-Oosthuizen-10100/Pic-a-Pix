import customtkinter as ctk
from tkinter import *
from tkinter.ttk import *

class SearchFrame(ctk.CTkFrame):

    def __init__(self, master, controller):
        super().__init__(master)

        h = 35
        
        self.controller = controller
        self.edt_search = ctk.CTkEntry(self, font=('JetBrains Mono', 14), height=h)
        self.edt_search.pack(side=LEFT, fill=X, expand=True, pady=5, padx=5)

        self.btn_search = ctk.CTkButton(self, font=('JetBrains Mono', 14), text="SEARCH", width=20, height=h)
        self.btn_search.pack(side=RIGHT, pady=5, padx=5)

class ImageTypeFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        h=20

        self.lbl_image_type = ctk.CTkLabel(self, text="Image Type", font=('JetBrains Mono', 11))
        self.lbl_image_type.pack(side=TOP, padx=5, pady=(5,0))

        self.cmb_image_type_var = ctk.IntVar(value="all")
        self.cmb_image_type = ctk.CTkComboBox(
            self,
            height=h,
            corner_radius=5,
            font=('JetBrains Mono', 10),
            values=["all", "photo", "illustration", "vector"],
            variable=self.cmb_image_type_var
        )

        self.cmb_image_type_var.set("all")
        self.cmb_image_type.pack(side=TOP, padx=5, pady=5)


class OptionsFrame(ctk.CTkFrame):

    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        h=20

        self.frm_image_type = ImageTypeFrame(self, controller)
        self.frm_image_type.pack(side=LEFT, padx=5, pady=5)

        self.edt_category = ctk.CTkEntry(self, font=('JetBrains Mono', 12), height=h, corner_radius=5)
        self.edt_category.pack(side=LEFT, padx=5, pady=5)

class MainWindow(ctk.CTk):

    def __init__(self, controller):
        super().__init__()
        
        self.controller = controller
        self.title('Pick-n-Pix')
        self.geometry('800x600')
        self.iconbitmap('.\\images\\application_icon.ico')
        self.minsize(250,250)

        self.search_frame = SearchFrame(self, controller)
        self.search_frame.pack(side=TOP, pady=(10,5), padx=10, fill=X)

        self.option_frame = OptionsFrame(self, controller)
        self.option_frame.pack(side=TOP, pady=(5,10), padx=10, fill=X)

class pnpView:
    
    def __init__(self, controller) -> None:
        self.root = MainWindow(controller)
        self.root.mainloop()
