from tkinter import messagebox, colorchooser
from customization import *
import customtkinter as ctk
import os

Buttons = []

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def create_tile(parent, title, description, btn_text, function):
    tile = ctk.CTkFrame(parent, corner_radius=10)
    tile.pack(pady=10, padx=10, fill="x")

    title_label = ctk.CTkLabel(tile, text=title, font=("Arial", 16, "bold"))
    title_label.pack(anchor="w", padx=10, pady=5)

    desc_label = ctk.CTkLabel(tile, text=description, font=("Arial", 12), wraplength=350)
    desc_label.pack(anchor="w", padx=10)

    Buttons.append(ctk.CTkButton(tile, text=btn_text, compound="left", command=function))
    Buttons[-1].pack(pady=10, padx=10, anchor="e")

def Theme_func():
    color = colorchooser.askcolor(title="Вибір кольору", parent=window)
    rgb_color = color[0]

    red = rgb_color[0]
    green = rgb_color[1]
    blue = rgb_color[2]

    Highlight().change(red, green, blue)

    restart = messagebox.askyesno('Перезапустити ПК?', 'Чи ти хочеш перезапустити ПК зараз?', parent=window)

    if restart:
        os.system("shutdown -r -t 0")

def Explorer_func():
    Buttons[2-1].configure(state = 'disabled')
    messagebox.showinfo('Зачекайте...', 'Зачекайте будь ласка, программа приміняє дії!', parent=window)
    ExplorerBlur().init()

def Console_func():
    Buttons[3-1].configure(state = 'disabled')
    messagebox.showinfo('Зачекайте...', 'Зачекайте будь ласка, программа приміняє дії!', parent=window)
    Console().init()

if __name__ == "__main__":
    window = ctk.CTk()
    window.geometry("1000x650")
    window.minsize(800, 500)
    window.title("WinFlex")
    create_tile(window, "Колір виділення", "Змінити колір виділення", "Налаштувати", Theme_func)
    create_tile(window, "Провідник", "Mica блюр для Windows Explorer", "Ініціалізувати", Explorer_func)
    create_tile(window, "Консоль", "Кастомізувати консоль", "Ініціалізувати", Console_func)
    window.mainloop()
