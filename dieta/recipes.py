import tkinter as tk
from tkinter import TclError, ttk
from options import WEEKS

def create_recipes_frame(container):
    frame = ttk.Frame(container)
    
    # grid layout for the recipes frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)
    
    # Weeks
    for i in range(4):
        ttk.Label(frame,
                  text='Week {0}:'.format(i)).grid(column=1, row=i, sticky=tk.W)
        button = ttk.Button(frame,
                            text='Week {0}:'.format(i))
        button.grid(column=2, row=i, sticky=tk.W)
        
    # Menu
    ttk.Button(frame, text='Menu').grid(column=0, row=0)
    ttk.Button(frame, text='Graph').grid(column=0, row=1)
    ttk.Button(frame, text='Products').grid(column=0, row=2)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)
    
    return frame