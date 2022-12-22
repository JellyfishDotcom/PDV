from tkinter import *
import customtkinter
import os
from PIL import Image
from contact import Contact

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Log_in(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # configure window
        self.title_esp='Inicio de Sesión'
        self.title_ing='Log In'
        self.title(self.title_esp)
        self.geometry(f"{550}x{270}")
        self.resizable(width=False, height=False)
        self.user = 'cris'
        self.password = '12345'

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.init_comp()

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
        self.log_in_btn = customtkinter.CTkButton(master=self.main_frame, text='Iniciar Sesión', command=self.log_in, image=self.log_in_image, compound='left')
        self.log_in_btn.grid(row=2, column=1, columnspan=3, padx=20, pady=20)

        # Contact button
        self.contact_btn = customtkinter.CTkButton(master=self.sidebar_frame, text='Contacto', command=self.open_contact_dialog, image=self.contact_image, compound='left')
        self.contact_btn.grid(row=1, column=0, padx=20, pady=10)

    def _init_labels(self):
        
        self.logo_label = customtkinter.CTkLabel(master=self.sidebar_frame, text="Control de Ventas", font=customtkinter.CTkFont(family='Gautami', size=16, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

    def _init_entrys(self):
        self.user_entry = customtkinter.CTkEntry(master=self.main_frame, width=200, height=30, placeholder_text='Usuario')
        self.user_entry.grid(row=0, column=2, padx=(10, 10), pady=(10, 10),  columnspan=3)

        self.password_entry = customtkinter.CTkEntry(master=self.main_frame, width=200, height=30, placeholder_text='Contraseña', show='*')
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
        if self.user_entry.get() == self.user:
            if self.password_entry.get() == self.password:
                print('Sesión iniciada uwu')
        else:
            print('Usuario o contraseña incorrectos')
            

if __name__ == '__main__':
    log_in = Log_in()
    log_in.mainloop()