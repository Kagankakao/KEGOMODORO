import tkinter as tk
from tkinter import messagebox

def reset_timer():
    if messagebox.askyesno("Reset Timer", "Are you sure you want to reset the timer?"):
        global hours, minute, second, crono_mode_activate, show_hours, saved_data, crono_reset, paused, note_writer_first_gap
        # Add your reset logic here
        crono_reset = True
        paused = False
        hours = 0
        minute = 0
        second = 0
        note_writer_first_gap = True
        # Reset other necessary variables and UI elements
        canvas.itemconfig(timer, text="00:00")
        floating_timer_label.config(text="00:00")
        # Cancel any running timers
        if 'count_downer' in globals():
            root.after_cancel(count_downer)
        if 'count_upper' in globals():
            root.after_cancel(count_upper)
        showinfo("Reset", "Timer has been reset.")

# Example usage of reset_timer function
if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=200, height=200)
    canvas.pack()
    timer = canvas.create_text(100, 100, text="00:00", font=("Helvetica", 24))
    floating_timer_label = tk.Label(root, text="00:00", font=("Helvetica", 24))
    floating_timer_label.pack()

    reset_button = tk.Button(root, text="Reset", command=reset_timer)
    reset_button.pack()

    root.mainloop()