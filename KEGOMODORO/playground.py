import tkinter as tk
from tkinter import messagebox

def open_popup():
    popup = tk.Toplevel(root)
    popup.title("Pop-Up Window")
    popup.geometry("300x200")

    label = tk.Label(popup, text="This is a pop-up window!", font=("Arial", 12))
    label.pack(pady=20)

    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)

# Main Window
root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

button = tk.Button(root, text="Open Pop-Up", command=open_popup)
button.pack(pady=20)

root.mainloop()
