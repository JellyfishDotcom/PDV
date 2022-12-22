from tkinter import *
from tkinter import messagebox
import customtkinter
import os
from PIL import Image
from contact import Contact
import mariadb
from data_base.data_base import Data_base
from main import Main

customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Log_in(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.db = Data_base()
        customtkinter.set_appearance_mode(self._select_theme())
        self._set_language(self._select_language())
        # configure window
        self.title(self.window_title_txt)
        self.geometry(f"{550}x{270}")
        self.resizable(width=False, height=False)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.init_comp()

    def _select_theme(self):
        self.db.query_sql(command='SELECT * from themes')
        themes = list()
        for theme in self.db.cur:
            themes.append(str(theme))
        if themes[0] == "('Light',)":
            return 'Light'
        if themes[0] == "('Dark',)":
            return 'Dark'
        if themes[0] == "('System',)":
            return 'System'

    def _select_language(self):
        self.db.query_sql(command='SELECT * from languages')
        languages = list()
        for language in self.db.cur:
            languages.append(str(language))
        print(languages)
        if languages[0] == "('English',)":
            return 'English'
        if languages[0] == "('Spanish',)":
            return 'Spanish'

    def _set_language(self, language):
        if language == 'English':
            self.window_title_txt = 'Log In'
            self.title_txt = 'Sales Control'
            self.contact_txt = 'Contact me'
            self.user_txt = 'User'
            self.password_txt = 'Password'
            self.log_in_txt = 'Log In'
            self.incorrect_title_txt = 'Incorrect user/password'
            self.incorrect_message_txt = 'The user that you provided does not exist or the password is not correct.'

        if language == 'Spanish':
            self.window_title_txt = 'Iniciar Sesión'
            self.title_txt = 'Control de Ventas'
            self.contact_txt = 'Contáctame'
            self.user_txt = 'Usuario'
            self.password_txt = 'Contraseña'
            self.log_in_txt = 'Iniciar Sesión'
            self.incorrect_title_txt = 'Usuario/contraseña incorrecto'
            self.incorrect_message_txt = 'El usuario que proporcionaste no existe o la contraseña es incorrecta.'


    def _init_figures(self):
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../figures/log_in")

        # Contact
        self.contact_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "contact.png")), size=(25, 25))

        # Log in
        self.log_in_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "log_in.png")), size=(25, 25))

        # Logo
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "LOGO_CIC.png")), size=(112, 115))
        self.logo_lbl = customtkinter.CTkLabel(master=self.sidebar_frame, text='', image=self.logo_image)
        self.logo_lbl.grid(row=3, column=0, padx=20, pady=20)

        # User
        self.user_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "user.png")), size=(50, 50))
        self.user_lbl = customtkinter.CTkLabel(master=self.main_frame, text='', image=self.user_image)
        self.user_lbl.grid(row=0, column=0, padx=20, pady=20)

        # Key
        self.password_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "key.png")), size=(50, 50))
        self.password_lbl = customtkinter.CTkLabel(master=self.main_frame, text='', image=self.password_image)
        self.password_lbl.grid(row=1, column=0, padx=20, pady=20)

    def _init_frames(self):
        # Sidebar frame
        self.sidebar_frame = customtkinter.CTkFrame(master=self, width=140, corner_radius=30)
        self.sidebar_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(3, weight=1)

        # Main frame
        self.main_frame = customtkinter.CTkFrame(master=self, width=300, corner_radius=30)
        self.main_frame.grid(row=0, column=1, rowspan=3, columnspan=3, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=6)

    def _init_buttons(self):
        # Log in button 
        self.log_in_btn = customtkinter.CTkButton(master=self.main_frame, text=self.log_in_txt, command=self.log_in, image=self.log_in_image, compound='left')
        self.log_in_btn.grid(row=2, column=1, columnspan=3, padx=20, pady=20)

        # Contact button
        self.contact_btn = customtkinter.CTkButton(master=self.sidebar_frame, text=self.contact_txt, command=self.open_contact_dialog, image=self.contact_image, compound='left')
        self.contact_btn.grid(row=1, column=0, padx=20, pady=10)

    def _init_labels(self):
        
        self.logo_label = customtkinter.CTkLabel(master=self.sidebar_frame, text=self.title_txt, font=customtkinter.CTkFont(family='Gautami', size=16, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

    def _init_entrys(self):
        self.user_entry = customtkinter.CTkEntry(master=self.main_frame, width=200, height=30, placeholder_text=self.user_txt)
        self.user_entry.grid(row=0, column=2, padx=(10, 10), pady=(10, 10),  columnspan=3)

        self.password_entry = customtkinter.CTkEntry(master=self.main_frame, width=200, height=30, placeholder_text=self.password_txt, show='*')
        self.password_entry.grid(row=1, column=2, padx=(10, 10), pady=(10, 10),  columnspan=3)

    def init_comp(self):
        self._init_frames()
        self._init_figures()
        self._init_buttons()
        self._init_labels()
        self._init_entrys()

    def open_contact_dialog(self):
        # dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        # print("CTkInputDialog:", dialog.get_input())
        self.contact = Contact(self)   
        self.contact.mainloop()   

    def log_in(self):
        try:
            users = list()
            self.db.query_sql(command='SELECT user FROM users')
            for user in self.db.cur:
                users.append(str(user))
            if str("('"+self.user_entry.get()+"',)") in users:
                passwords = list()
                try:
                    self.db.query_sql(command=str("SELECT password FROM users WHERE user='"+self.user_entry.get()+"'"))
                    for password in self.db.cur:
                        passwords.append(str(password))
                    if str("('"+self.password_entry.get()+"',)") == passwords[0]:
                        self.withdraw()
                        self.main = Main(self)

                    else:
                        messagebox.showerror(title=self.incorrect_title_txt, message=self.incorrect_message_txt)
                except mariadb.Error as e:
                    print(f'Error: {e}')
            if str("('"+self.user_entry.get()+"',)") not in users:
                messagebox.showerror(title=self.incorrect_title_txt, message=self.incorrect_message_txt)

        except mariadb.Error as e:
            print(f'Error {e}')
            

if __name__ == '__main__':
    log_in = Log_in()
    log_in.mainloop()