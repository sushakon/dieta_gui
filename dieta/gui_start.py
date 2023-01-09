import tkinter as tk
from tkinter import Tk
from tkinter import TclError, ttk
from options import create_options_frame, create_weeks_next_frame, CONFIRM
from recipes import create_recipes_frame

def create_start_window():
    root = Tk()
    root.title('Replace')
    root.resizable(0, 0)
    try:
        # windows only (remove the minimize/maximize button)
        root.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    # layout on the root window
    
    if CONFIRM == False:
        root.columnconfigure(0, weight=4)
        root.columnconfigure(1, weight=1)

        input_frame = create_options_frame(root)
        input_frame.grid(column=0, row=0)

        button_frame = create_weeks_next_frame(root)
        button_frame.grid(column=1, row=0)
    else:
        root.columnconfigure(0, weight=4)
        root.columnconfigure(1, weight=1)
        
        recipe_frame = create_recipes_frame(root)
        recipe_frame.grid(column=0, row=0)

    root.mainloop()