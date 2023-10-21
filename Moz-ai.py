# october-2023 - python3 - am1rw4ck3r
# trying to make funni ai with customtkinter /
# just for improving my knowledge about this library

import customtkinter
#import tkinter.messagebox
import tkinter
from PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window basics
        self.title("Moz ai")
        self.geometry(f"{600}x{300}")

        # configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0,1), weight=1)

        # sidebar frame
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=1, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((0,1), weight=1)
        self.logo = customtkinter.CTkImage(dark_image=Image.open("/home/amir/Downloads/moz.png"), size=(80,80))
        self.logo.grid(row=0, column=0, padx=20, pady=(20,10))
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, image=self.logo, text="Moz ai")



if __name__ == "__main__":
    app = App()
    app.mainloop()
