import customtkinter as ctk

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

checkbox1 = ctk.CTkCheckBox(frame1, text="Чекбокс 1")
checkbox1.pack(anchor="w", pady=5)

checkbox2 = ctk.CTkCheckBox(frame1, text="Чекбокс 2")
checkbox2.pack(anchor="w", pady=5)

frame2 = ctk.CTkFrame(tabview.tab("Frame 2"))
frame2.pack(fill="both", expand=True, padx=10, pady=10)

checkbox3 = ctk.CTkCheckBox(frame2, text="Чекбокс 3")
checkbox3.pack(anchor="w", pady=5)

checkbox4 = ctk.CTkCheckBox(frame2, text="Чекбокс 4")
checkbox4.pack(anchor="w", pady=5)

root.mainloop()
