from tkinter import *
import customtkinter
import os
from PIL import Image
import sys
from data_base.data_base import Data_base

customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue

class Main(customtkinter.CTkToplevel):
    def __init__(self, log_in):
        super().__init__()
        self.db = Data_base()
        customtkinter.set_appearance_mode(self._select_theme())
        self._set_language(self._select_language())

        # configure window
        self.title_esp='Punto de venta: Vista princpal.'
        self.title_ing='Contact'
        self.title(self.title_esp)
        self.geometry(f"{1350}x{720}")
        self.resizable(width=False, height=False)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        self.log_in = log_in
        self.init_comp()

    def _select_theme(self):
        self.db.query_sql(command='SELECT * from themes')
        themes = list()
        for id_theme, theme in self.db.cur:
            themes.append(str(theme))
        return themes[0]

    def _save_theme(self, new_theme:str):
        command = str("UPDATE themes SET theme='"+new_theme+"' WHERE id_theme=1")
        self.db.modify_sql(command=command)

    def _select_language(self):
        self.db.query_sql(command='SELECT * from languages')
        languages = list()
        for id_language, language in self.db.cur:
            languages.append(str(language))
        return languages[0]

    def _save_language(self, language:str):
        command = str("UPDATE languages SET language='"+language+"' WHERE id_language=1")
        self.db.modify_sql(command=command)

    def _set_language(self, language):
        if language == 'English':
            pass
        
        if language == 'Spanish':
            pass

    def change_language_mode_event(self, new_language_mode:str):
        self._save_language(str(new_language_mode))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
        new_theme = str(customtkinter.get_appearance_mode())
        self._save_theme(new_theme)
        

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
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../figures/main")

        # Logo
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "LOGO_CIC.png")), size=(112, 112))
        self.logo_lbl = customtkinter.CTkLabel(master=self.sidebar_frame, text='', image=self.logo_image)
        self.logo_lbl.grid(row=0, column=0, padx=20, pady=20)

        # Sell
        self.sell_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "sell.png")), size=(25, 25))

        # Cut
        self.dinner_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "cut.png")), size=(25, 25))
        

    def _init_buttons(self):
        # Venta 
        self.venta_btn = customtkinter.CTkButton(master=self.sidebar_frame, text='Venta', command=self.sold, image=self.sell_image, compound='left')
        self.venta_btn.grid(row=2, column=0, columnspan=3, padx=20, pady=20)

        # Corte
        self.corte_btn = customtkinter.CTkButton(master=self.sidebar_frame, text='Corte', command=self.finish, image=self.dinner_image, compound='left')
        self.corte_btn.grid(row=3, column=0, padx=20, pady=10)
        

        # Language option menu
        self.appearance_language_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Spanish", "English"],
                                                                       command=self.change_language_mode_event)
        self.appearance_language_optionemenu.grid(row=4, column=0, padx=20, pady=(10, 10))
        self.appearance_language_optionemenu.set(str(self._select_language()))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=5, column=0, padx=20, pady=(10, 10))
        self.appearance_mode_optionemenu.set(str(customtkinter.get_appearance_mode()))

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

    def sold(self):
        pass

    def finish(self):
        pass

if __name__ == '__main__':
    main = Main()
    main.mainloop()