import tkinter as tk

def close_window(event=None):
    """Close the window."""
    root.quit()

# Create the main window
root = tk.Tk()

# Set the window size (e.g., 300x200) and make it non-resizable
root.geometry("300x200")
root.resizable(False, False)  # Lock the window size

# Set the background color to gray
root.config(bg='gray')

# Add some content
label = tk.Label(root, text="This is a locked window.", bg='gray', fg='white')
label.pack(expand=True)

# Bind the close event (optional)
root.bind("<Control-q>", close_window)  # Close with Ctrl + Q

# Run the Tkinter event loop
root.mainloop()
