import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

# Frame (menu or container)
menu_frame = tk.Frame(root, width=200, height=100, bg='lightblue')
menu_frame.place(x=100, y=100)
menu_frame.pack_propagate(False)

# Button that belongs to the frame, but is positioned outside
btn = tk.Button(menu_frame, text="Still My Frame")
btn.place(x=50, y=120)  # Y is beyond frame's height

root.mainloop()