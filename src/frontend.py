import customtkinter as ctk
from backend import *

Buttons = []

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("1000x650")
root.minsize(800, 500)
root.title("WinFlex")

def create_tile(parent, title, description, function):
    tile = ctk.CTkFrame(parent, corner_radius=10)
    tile.pack(pady=10, padx=10, fill="x")

    title_label = ctk.CTkLabel(tile, text=title, font=("Arial", 16, "bold"))
    title_label.pack(anchor="w", padx=10, pady=5)

    desc_label = ctk.CTkLabel(tile, text=description, font=("Arial", 12), wraplength=350)
    desc_label.pack(anchor="w", padx=10)

    Buttons.append(ctk.CTkButton(tile, text="Налаштувати", compound="left", command=function))
    Buttons[-1].pack(pady=10, padx=10, anchor="e")

create_tile(root, "Тема оформлення", "Змінити колірну схему оформлення", lambda: print("HELLO"))
create_tile(root, "Провідник", "Mica блюр для Windows Explorer", lambda: print("HELL0"))
create_tile(root, "Консоль", "Кастомізувати консоль", lambda: print("HELL"))

root.mainloop()
