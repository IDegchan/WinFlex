from multiprocessing import Process
from tkinter import messagebox
from CTkColorPicker import *
from customization import *
import customtkinter as ctk
from PIL import ImageColor
import os

Buttons = []

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("1000x650")
root.minsize(800, 500)
root.title("WinFlex")

def create_tile(parent, title, description, btn_text, function):
    tile = ctk.CTkFrame(parent, corner_radius=10)
    tile.pack(pady=10, padx=10, fill="x")

    title_label = ctk.CTkLabel(tile, text=title, font=("Arial", 16, "bold"))
    title_label.pack(anchor="w", padx=10, pady=5)

    desc_label = ctk.CTkLabel(tile, text=description, font=("Arial", 12), wraplength=350)
    desc_label.pack(anchor="w", padx=10)

    Buttons.append(ctk.CTkButton(tile, text=btn_text, compound="left", command=function))
    Buttons[-1].pack(pady=10, padx=10, anchor="e")

def _init_console(): Console().init()
def _init_explorer(): ExplorerBlur().init()

def Theme_func():
    pick_color = AskColor(title="Вибір кольору")

    hex_color = pick_color.get()
    rgb_color = ImageColor.getcolor(hex_color, "RGB")

    red = rgb_color[0]
    green = rgb_color[1]
    blue = rgb_color[2]

    Highlight().change(red, green, blue)

    restart = messagebox.askyesno('Перезапустити ПК?', 'Чи ти хочеш перезапустити ПК зараз?', parent=root)

    if restart:
        os.system("shutdown -r -t 0")

def Explorer_func():
    Buttons[2-1].configure(state = 'disabled')
    p = Process(name="Initialize console", target=_init_explorer)
    p.start()

def Console_func():
    Buttons[3-1].configure(state = 'disabled')
    p = Process(name="Initialize console", target=_init_console)
    p.start()

create_tile(root, "Колір виділення", "Змінити колір виділення", "Налаштувати", Theme_func)
create_tile(root, "Провідник", "Mica блюр для Windows Explorer", "Ініціалізувати", Explorer_func)
create_tile(root, "Консоль", "Кастомізувати консоль", "Ініціалізувати", Console_func)

if __name__ == "__main__":
    root.mainloop()
