from tkinter import *
import customtkinter
import os
from PIL import Image

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

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.init_comp()

    def init_comp(self):
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=30)
        self.sidebar_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(3, weight=1)

        self.main_frame = customtkinter.CTkFrame(self, width=300, corner_radius=30)
        self.main_frame.grid(row=0, column=1, rowspan=3, columnspan=3, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=6)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CONTROL DE VENTAS", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.contact_btn = customtkinter.CTkButton(self.sidebar_frame, text='Contacto', command=self.open_contact_dialog)
        self.contact_btn.grid(row=1, column=0, padx=20, pady=10)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../figures")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "LOGO_CIC.png")), size=(125, 125))
        self.logo_lbl = customtkinter.CTkLabel(self.sidebar_frame, text='', image=self.logo_image)
        self.logo_lbl.grid(row=3, column=0, padx=20, pady=20)

        self.user_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "user.png")), size=(75, 75))
        self.user_lbl = customtkinter.CTkLabel(self.main_frame, text='', image=self.user_image)
        self.user_lbl.grid(row=0, column=0, padx=20, pady=20)

        self.password_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "key.png")), size=(75, 75))
        self.password_lbl = customtkinter.CTkLabel(self.main_frame, text='', image=self.password_image)
        self.password_lbl.grid(row=1, column=0, padx=20, pady=20)

        self.user_entry = customtkinter.CTkEntry(self.main_frame, width=200, height=18, placeholder_text='Usuario')
        #self.user_entry.pack(padx=10, pady=10)
        self.user_entry.grid(row=0, column=2, padx=(10, 10), pady=(10, 10),  columnspan=3)

        self.password_entry = customtkinter.CTkEntry(self.main_frame, width=200, height=18, placeholder_text='Password', show='*')
        self.password_entry.grid(row=1, column=2, padx=(10, 10), pady=(10, 10),  columnspan=3)

        self.log_in_btn = customtkinter.CTkButton(self.main_frame, text='Iniciar Sesión', command=self.log_in)
        self.log_in_btn.grid(row=2, column=1, columnspan=3, padx=20, pady=0)

    def init_frames(self):
        pass

    def init_buttons(self):
        pass

    def open_contact_dialog(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def log_in(self):
        if self.password_entry._textvariable == '1':
            print('Sesión iniciada alv')

if __name__ == '__main__':
    log_in = Log_in()
    log_in.mainloop()