import os
import customtkinter as ctk
from PIL import Image

# Налаштування теми
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Головне вікно
app = ctk.CTk()
app.geometry("600x400")
app.title("WinFlex - Customization Tool")

# Фрейм для плиток
tile_frame = ctk.CTkFrame(app)
tile_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Перевірка наявності файлу іконки
icon_path = "icon.png"
if not os.path.exists(icon_path):
    print(f"Файл {icon_path} не знайдено! Переконайтеся, що він у правильній папці.")
    icon = None
else:
    icon = ctk.CTkImage(dark_image=Image.open(icon_path), size=(40, 40))

# Функція створення плитки
def create_tile(parent, title, description):
    tile = ctk.CTkFrame(parent, corner_radius=10)
    tile.pack(pady=10, padx=10, fill="x")

    # Лейбл заголовка
    title_label = ctk.CTkLabel(tile, text=title, font=("Arial", 16, "bold"))
    title_label.pack(anchor="w", padx=10, pady=5)

    # Лейбл опису
    desc_label = ctk.CTkLabel(tile, text=description, font=("Arial", 12), wraplength=400)
    desc_label.pack(anchor="w", padx=10)

    # Кнопка дії
    action_button = ctk.CTkButton(tile, text="Налаштувати", image=icon, compound="left")
    action_button.pack(pady=10, padx=10, anchor="e")

# Додавання плиток
create_tile(tile_frame, "Тема оформлення", "Змінити колірну схему Windows.")
create_tile(tile_frame, "Іконки", "Налаштування системних іконок.")
create_tile(tile_frame, "Анімації", "Управління анімаціями Windows.")

# Запуск програми
app.mainloop()
