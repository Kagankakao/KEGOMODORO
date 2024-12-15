import tkinter as tk

def toggle():
    if switch_button.config('text')[-1] == 'OFF':
        switch_button.config(text='ON', bg='green')
    else:
        switch_button.config(text='OFF', bg='red')

root = tk.Tk()
root.title("Switch Button")

switch_button = tk.Button(root, text="OFF", bg="black", width=4, height=4, command=toggle)
switch_button.pack()

root.mainloop()
