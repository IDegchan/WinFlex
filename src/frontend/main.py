import customtkinter as ctk

root = ctk.CTk()

tabview = ctk.CTkTabview(root)
tabview.pack(expand=True, fill="both")

tabview.add("Frame 1")
tabview.add("Frame 2")

frame1 = ctk.CTkFrame(tabview.tab("Frame 1"), width=200, height=200)
frame1.grid(row=0, column=0, padx=20, pady=20)
frame1.configure(bg_color="red")

frame2 = ctk.CTkFrame(tabview.tab("Frame 2"), width=200, height=200)
frame2.grid(row=0, column=0, padx=20, pady=20)
frame2.configure(bg_color="blue")

root.mainloop()
