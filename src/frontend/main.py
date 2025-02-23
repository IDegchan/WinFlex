import os
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("400x300")
root.minsize(400, 300)
root.title("WinFlex")

tabview = ctk.CTkTabview(root)
tabview.pack(expand=True, fill="both")
tabview.add("Explore")
tabview.add("Settings")

Explore = ctk.CTkFrame(tabview.tab("Explore"))
Explore.pack(fill="both", expand=True, padx=10, pady=10)

Settings = ctk.CTkFrame(tabview.tab("Settings"))
Settings.pack(fill="both", expand=True, padx=10, pady=10)


def create_tile(parent, title, description):
    tile = ctk.CTkFrame(parent, corner_radius=10)
    tile.pack(pady=10, padx=10, fill="x")

    title_label = ctk.CTkLabel(tile, text=title, font=("Arial", 16, "bold"))
    title_label.pack(anchor="w", padx=10, pady=5)

    desc_label = ctk.CTkLabel(tile, text=description, font=("Arial", 12), wraplength=350)
    desc_label.pack(anchor="w", padx=10)

    action_button = ctk.CTkButton(tile, text="Завантажити", compound="left")
    action_button.pack(pady=10, padx=10, anchor="e")

create_tile(Explore, "Тема оформлення", "Змінити колірну схему Windows.")
create_tile(Explore, "Іконки", "Налаштування системних іконок.")
create_tile(Explore, "Анімації", "Управління анімаціями Windows.")

root.mainloop()
