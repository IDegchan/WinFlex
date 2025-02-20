import json
import os

class ShopItem:
    def __init__(self, name, description, prog_dir):
        self.name = name
        self.description = description
        self.prog_dir = prog_dir

    def use(self):
        raise NotImplementedError("Цей предмет не має дії!")

class FileHandlerItem(ShopItem):
    def __init__(self, name, description, file_path, content, prog_dir):
        super().__init__(name, description, prog_dir)
        self.file_path = file_path
        self.content = content

    def use(self):
        """Створює файл, якщо він не існує, і записує вміст у будь-якому випадку."""
        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write(self.content)
        print(f"[{self.name}] Файл {self.file_path} створено або змінено!")

def load_items_from_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    items = []
    for item_data in data:
        item_type = item_data["type"]
        if item_type == "file_handler":
            item = FileHandlerItem(
                item_data["name"], item_data["description"],
                item_data["file_path"], item_data["content"], item_data["program_directory"]
            )
        else:
            continue
        
        items.append(item)

    return items

# Завантажуємо предмети
shop_items = load_items_from_json("../items.json")

# Використовуємо предмети
for item in shop_items:
    print("\n" + "-" * 50)
    print(f"Використовую: {item.name}")
    print(f"{item.description}")
    print(f"{item.prog_dir}")
    print(f"{item.file_path}")
    print(f"{item.content}")
    print("-" * 50 + "\n")
