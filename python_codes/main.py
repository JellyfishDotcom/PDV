from tkinter import *
import customtkinter
import os
from PIL import Image
from window import Window
import sys

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue

class Main(Window, customtkinter.CTkToplevel):
    def __init__(self, log_in):
        super().__init__()
        # configure window
        self.title_esp='Punto de venta: Vista princpal.'
        self.title_ing='Contact'
        self.title(self.title_esp)
        self.geometry(f"{1100}x{580}")
        self.resizable(width=False, height=False)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        self.log_in = log_in
        self.init_comp()

    def change_language_mode_event(self, new_language_mode: str):
        pass
        #customtkinter.set_appearance_mode(new_appearance_mode)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def _on_closing(self):
        # self.log_in.contact_btn.configure(state='enabled')
        sys.exit()

    def _init_frames(self):
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=950, height=350)
        self.tabview.grid(row=0, column=1,columnspan=3, padx=(10, 10), pady=(0, 0))
        self.tabview.add("Ventas")
        self.tabview.add("Estadísticas")
        self.tabview.add("Administración")
        self.tabview.tab("Ventas").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Estadísticas").grid_columnconfigure(0, weight=1)
 
    def _init_figures(self):
        pass

    def _init_buttons(self):
        self.appearance_language_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Spanish", "English"],
                                                                       command=self.change_language_mode_event)
        self.appearance_language_optionemenu.grid(row=4, column=0, padx=20, pady=(10, 10))
        self.appearance_language_optionemenu.set("Spanish")

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=5, column=0, padx=20, pady=(10, 10))
        self.appearance_mode_optionemenu.set("Dark")

    def _init_labels(self):
        pass

    def _init_entrys(self):
        pass


    def init_comp(self):
        self._init_frames()
        self._init_figures()
        self._init_buttons()
        self._init_labels()
        self._init_entrys()
        self.protocol('WM_DELETE_WINDOW', self._on_closing)
        self.mainloop()

if __name__ == '__main__':
    main = Main()
    main.mainloop()