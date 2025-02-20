import customtkinter as ctk

def change_selection_color(widget, bg="#34eb8c", fg="#000000"):
    """Меняет цвет выделения текста"""
    widget._textbox.tag_configure("sel", background=bg, foreground=fg)