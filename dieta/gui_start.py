import tkinter as tk
from tkinter import Tk
from tkinter import TclError, ttk
from options import create_options_frame, create_weeks_next_frame, confirm, options
from recipes import create_recipes_frame

def hide_frame(frame):
    frame.destroy()

def create_start_window():
    global confirm
    
    root = tk.Tk()
    root.title("Dieta")
    root.geometry("800x500")
    root.resizable(width=False, height=False)
    root.configure(bg="#111111")
    
    try:
        # windows only (remove the minimize/maximize button)
        root.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    # layout on the root window
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)
    
    if options == True:
        input_frame = create_options_frame(root)
        input_frame.grid(column=0, row=0)

        button_frame = create_weeks_next_frame(root)
        button_frame.grid(column=1, row=0)
        if confirm == True:
            hide_frame(input_frame)
            hide_frame(button_frame)
    else:
        print(confirm)
        recipe_frame = create_recipes_frame(root)
        recipe_frame.grid(column=0, row=0)

    root.mainloop()