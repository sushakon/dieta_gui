import tkinter as tk
from tkinter import Tk
from tkinter import TclError, ttk
# from options import create_options_frame, create_weeks_next_frame, confirm, options
from recipes import create_recipes_frame
from options import create_options_frame

options = True

def hide_frame(frame):
    frame.destroy()

def create_start_window():
    global confirm
    global options
    
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
        create_recipes_frame(root)
        create_options_frame(root)

    root.mainloop()