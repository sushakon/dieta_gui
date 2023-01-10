import tkinter as tk
from tkinter import TclError, ttk

weights = [0, 0, 0, 0]
weeks = 0
confirm = False
options = True

weight_options = [1, 2, 3, 4]

def create_options_frame(container):

    frame = ttk.Frame(container)
    
    #label
    label = ttk.Label(frame, text='Priorities (1-4):').grid(column=0, row=0, sticky=tk.W)

    # grid layout for the options frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=4)

    # Calories
    option_var_cal = tk.IntVar()
    option_var_cal.set(1)
    ttk.Label(frame, text='Calories:').grid(column=0, row=1, sticky=tk.W)
    calories  = ttk.OptionMenu(
            frame,
            option_var_cal,
            weight_options[0],
            *weight_options,
            command=lambda _: option_changed_cal(option_var_cal.get()))
    calories.grid(column=1, row=1, sticky=tk.W)

    # Fat
    option_var_f = tk.IntVar()
    option_var_f.set(1)
    print(option_var_f.get())
    ttk.Label(frame, text='Fat:').grid(column=0, row=2, sticky=tk.W)
    fat  = ttk.OptionMenu(
            frame,
            option_var_f,
            weight_options[0],
            *weight_options,
            command=lambda _: option_changed_f(option_var_f.get()))
    print(option_var_f.get())
    fat.grid(column=1, row=2, sticky=tk.W)

    # Carbs
    option_var_c = tk.IntVar()
    option_var_c.set(1)
    ttk.Label(frame, text='Carbs:').grid(column=0, row=3, sticky=tk.W)
    carbs  = ttk.OptionMenu(
            frame,
            option_var_c,
            weight_options[0],
            *weight_options,
            command=lambda _: option_changed_c(option_var_c.get()))
    carbs.grid(column=1, row=3, sticky=tk.W)

    # Protein
    option_var_p = tk.IntVar()
    option_var_p.set(1)
    ttk.Label(frame, text='Protein:').grid(column=0, row=4, sticky=tk.W)
    protein  = ttk.OptionMenu(
            frame,
            option_var_p,
            weight_options[0],
            *weight_options,
            command=lambda _: option_changed_p(option_var_p.get()))
    protein.grid(column=1, row=4, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame

def create_weeks_next_frame(container):
    
    def is_confirmed():
        global confirm
        confirm = True
    
    def is_options():
        global options
        options = False
    
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)
    
    #label
    label = ttk.Label(frame, text='Number of weeks:')
    label.grid(column=0, row=0, sticky=tk.W)

    confirm = ttk.Button(frame,
                         text='Confirm',
                         command= lambda: [is_confirmed(), is_options])
    confirm.grid(column=0, row=5)
    
    # Number of weeks radiobox
    weeks = tk.IntVar()
    weeks_check = ttk.Radiobutton(
        frame,
        variable=weeks,
        text='1 week',
        value=1,
        command=option_changed_week(weeks.get()))
    weeks_check.grid(column=0, row=1, sticky=tk.W)
    weeks_check = ttk.Radiobutton(
        frame,
        variable=weeks,
        text='2 weeks',
        value=2,
        command=option_changed_week(weeks.get()))
    weeks_check.grid(column=0, row=2, sticky=tk.W)
    weeks_check = ttk.Radiobutton(
        frame,
        variable=weeks,
        text='3 weeks',
        value=3,
        command=option_changed_week(weeks.get()))
    weeks_check.grid(column=0, row=3, sticky=tk.W)
    weeks_check = ttk.Radiobutton(
        frame,
        variable=weeks,
        text='4 weeks',
        value=4,
        command=option_changed_week(weeks.get()))
    weeks_check.grid(column=0, row=4, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)
        
    return frame


def option_changed_cal(val):
    global weights
    weights[0] = (5 - int(val))

def option_changed_f(val):
    global weights
    weights[1] = (5 - int(val))
        
def option_changed_c(val):
    global weights
    weights[2] = (5 - int(val))
    
def option_changed_p(val):
    global weights
    weights[3] = (5 - int(val))
    
def option_changed_week(val):
    global weeks
    weeks = int(val)        