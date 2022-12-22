from tkinter import *
import customtkinter
import os
from PIL import Image
import webbrowser

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue

class Contact(customtkinter.CTkToplevel):
    def __init__(self, log_in):
        super().__init__()
        # configure window
        self.title_esp='Contacto'
        self.title_ing='Contact'
        self.title(self.title_esp)
        self.geometry(f"{400}x{200}")
        self.resizable(width=False, height=False)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        self.log_in = log_in
        self.log_in.contact_btn.configure(state='disabled')
        self.init_comp_contact()
    
    def on_closing(self):
        self.log_in.contact_btn.configure(state='enabled')
        self.destroy()

    def init_comp_contact(self):
        figure_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../figures/contact")
        
        self.jellyfishDotcom_image = customtkinter.CTkImage(Image.open(os.path.join(figure_path, "jellyfishDotcom.jpg")), size=(100, 100))
        self.logoJF_lbl = customtkinter.CTkLabel(master=self, text='JellyfishDotcom', image=self.jellyfishDotcom_image, compound='top')
        self.logoJF_lbl.grid(row=0, column=0, padx=20, pady=20)

        # Main frame
        self.buttons_frame = customtkinter.CTkFrame(master=self, width=300, corner_radius=30)
        self.buttons_frame.grid(row=0, column=1, rowspan=3, columnspan=3, sticky="nsew")
        self.buttons_frame.grid_rowconfigure(6, weight=6)

        self.github_image = customtkinter.CTkImage(Image.open(os.path.join(figure_path, "github.png")), size=(30, 30))
        self.github_btn = customtkinter.CTkButton(master=self.buttons_frame, text='Github', command=self.github_connect, image=self.github_image, compound='left')
        self.github_btn.pack(pady=5, padx=10)

        self.instagram_image = customtkinter.CTkImage(Image.open(os.path.join(figure_path, "instagram.png")), size=(30, 30))
        self.instagram_btn = customtkinter.CTkButton(master=self.buttons_frame, text='Instagram', command=self.instagram_connect, image=self.instagram_image, compound='left')
        self.instagram_btn.pack(pady=5, padx=10)

        self.reddit_image = customtkinter.CTkImage(Image.open(os.path.join(figure_path, "reddit.png")), size=(30, 30))
        self.reddit_btn = customtkinter.CTkButton(master=self.buttons_frame, text='Reddit', command=self.reddit_connect, image=self.reddit_image, compound='left')
        self.reddit_btn.pack(pady=5, padx=10)

        self.twitter_image = customtkinter.CTkImage(Image.open(os.path.join(figure_path, "twitter.png")), size=(30, 30))
        self.twitter_btn = customtkinter.CTkButton(master=self.buttons_frame, text='Twitter', command=self.twitter_connect, image=self.twitter_image, compound='left')
        self.twitter_btn.pack(pady=5, padx=10)

        self.protocol('WM_DELETE_WINDOW', self.on_closing)
        
    def github_connect(self):
        webbrowser.open("https://github.com/JellyfishDotcom", new=0, autoraise=True)

    def instagram_connect(self):
        webbrowser.open("https://www.instagram.com/saulhv6", new=0, autoraise=True)

    def reddit_connect(self):
        webbrowser.open("https://www.reddit.com/user/JellyfishDotcom", new=0, autoraise=True)

    def twitter_connect(self):
        webbrowser.open("https://twitter.com/csaulhv", new=0, autoraise=True)

if __name__ == '__main__':
    contact = Contact()
    contact.mainloop()