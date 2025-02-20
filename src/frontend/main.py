import os
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("400x300")
root.minsize(400, 300)
root.title("WinFlex")

tabview = ctk.CTkTabview(root)
tabview.pack(expand=True, fill="both")

tabview.add("Frame 1")
tabview.add("Frame 2")

frame1 = ctk.CTkFrame(tabview.tab("Frame 1"))
frame1.pack(fill="both", expand=True, padx=10, pady=10)

frame2 = ctk.CTkFrame(tabview.tab("Frame 2"))
frame2.pack(fill="both", expand=True, padx=10, pady=10)

icon_path = "icon.png"
if not os.path.exists(icon_path):
    print(f"Файл {icon_path} не знайдено! Переконайтеся, що він у правильній папці.")
    icon = None
else:
    icon = ctk.CTkImage(dark_image=Image.open(icon_path), size=(40, 40))

def create_tile(parent, title, description):
    tile = ctk.CTkFrame(parent, corner_radius=10)
    tile.pack(pady=10, padx=10, fill="x")

    title_label = ctk.CTkLabel(tile, text=title, font=("Arial", 16, "bold"))
    title_label.pack(anchor="w", padx=10, pady=5)

    desc_label = ctk.CTkLabel(tile, text=description, font=("Arial", 12), wraplength=350)
    desc_label.pack(anchor="w", padx=10)

    action_button = ctk.CTkButton(tile, text="Налаштувати", image=icon, compound="left")
    action_button.pack(pady=10, padx=10, anchor="e")

create_tile(frame1, "Тема оформлення", "Змінити колірну схему Windows.")
create_tile(frame1, "Іконки", "Налаштування системних іконок.")
create_tile(frame1, "Анімації", "Управління анімаціями Windows.")

root.mainloop()
