import tkinter as tk
from tkinter import TclError, ttk


###############################################################################
# OPTIONS #####################################################################
###############################################################################

weights = [0, 0, 0, 0]
weeks = 0
confirm = False
options = True

weight_options = [1, 2, 3, 4]

def hide_frame(frame):
    frame.destroy()

def create_options_frame(container):
    global options
    options = True
    
    if options == True:
               
        frame = tk.Frame(container,
                          bg="#191919",
                          width=790,
                          height=490, bd=0)
        #label                
        empty = tk.Label(frame,
                         width=108,
                         height=3,
                         bg="#1d1947")
        empty.grid(columnspan=4, row=0, sticky=tk.W)
        
        prefer = tk.Label(frame,
                         text='Dostosuj swoje preferencje',
                         bg="#1d1947", fg="#cbcbcb",
                         font=("Calibri", 20))
        prefer.grid(column=1, row=0, sticky=tk.W)
        
        # grid layout for the options frame
        # frame.columnconfigure(0, weight=1)
        # frame.columnconfigure(0, weight=4)
        frame.place(x=15, y=10)

        label = tk.Label(frame,
                         text='Priorytet składników',
                         bg="#191919", fg="#cbcbcb",
                         font=("Calibri", 20))
        label.grid(column=0, row=1, sticky=tk.W)

        # Calories
        option_var_cal = tk.IntVar()
        option_var_cal.set(1)
        tk.Label(frame, text='Calories:',
                 bg="#191919", fg="#cbcbcb",
                 font=("Calibri", 20)).grid(column=0, row=2, sticky=tk.W)
        calories  = tk.OptionMenu(
                frame,
                option_var_cal,
                *weight_options,
                command=lambda _: option_changed_cal(option_var_cal.get()))
        calories.grid(column=1, row=2, sticky=tk.W)
        calories.config(width=10,
                     bg="#191919", fg="#cbcbcb",
                     font=("Calibri", 20),
                     activebackground="#191919",
                     activeforeground="#cbcbcb")
        calories['menu'].config(bg="#191919")

        # Fat
        option_var_f = tk.IntVar()
        option_var_f.set(1)
        tk.Label(frame, text='Fat:',
                 bg="#191919", fg="#cbcbcb",
                 font=("Calibri", 20)).grid(column=0, row=3, sticky=tk.W)
        fat  = tk.OptionMenu(
                frame,
                option_var_f,
                *weight_options,
                command=lambda _: option_changed_f(option_var_f.get()))
        fat.grid(column=1, row=3, sticky=tk.W)
        fat.config(width=10,
                     bg="#191919", fg="#cbcbcb",
                     font=("Calibri", 20),
                     activebackground="#191919",
                     activeforeground="#cbcbcb")
        fat['menu'].config(bg="#191919")

        # Carbs
        option_var_c = tk.IntVar()
        option_var_c.set(1)
        tk.Label(frame, text='Carbs:',
                 bg="#191919", fg="#cbcbcb",
                 font=("Calibri", 20)).grid(column=0, row=4, sticky=tk.W)
        carbs  = tk.OptionMenu(
                frame,
                option_var_c,
                *weight_options,
                command=lambda _: option_changed_c(option_var_c.get()))
        carbs.grid(column=1, row=4, sticky=tk.W)
        carbs.config(width=10,
                     bg="#191919", fg="#cbcbcb",
                     font=("Calibri", 20),
                     activebackground="#191919",
                     activeforeground="#cbcbcb")
        carbs['menu'].config(bg="#191919")

        # Protein
        option_var_p = tk.IntVar()
        option_var_p.set(1)
        tk.Label(frame, text='Protein:',
                 bg="#191919", fg="#cbcbcb",
                 font=("Calibri", 20)).grid(column=0, row=5, sticky=tk.W)
        protein  = tk.OptionMenu(
                frame,
                option_var_p,
                *weight_options,
                command=lambda _: option_changed_p(option_var_p.get()))
        protein.grid(column=1, row=5, sticky=tk.W)
        protein.config(width=10,
                        bg="#191919", fg="#cbcbcb",
                        font=("Calibri", 20),
                        activebackground="#191919",
                        activeforeground="#cbcbcb")
        protein['menu'].config(bg="#191919")
        
        
        #buttons
        label = tk.Label(frame,
                         text='Ilość tygodni',
                         bg="#191919", fg="#cbcbcb",
                         font=("Calibri", 20))
        label.grid(column=3, row=1, sticky=tk.W)

        confirm = tk.Button(frame,
                            text='Confirm',
                            font=("Calibri", 20),
                            bg="#333241", fg="#cbcbcb",
                            activebackground="#333241",
                            activeforeground="#cbcbcb",
                            command= lambda: [is_confirmed(), is_options(), hide_frame(frame), create_recipes_frame(container)])
        confirm.grid(column=3, row=8)
        
        empty = tk.Label(frame,
                    width=108,
                    height=3,
                    bg="#1d1947")
        empty.grid(columnspan=4, row=6, sticky=tk.W)
        empty = tk.Label(frame,
            width=108,
            height=1,
            bg="#1d1947")
        empty.grid(columnspan=4, row=7, sticky=tk.W)
        
        # Number of weeks radiobox
        weeks = tk.IntVar()
        weeks_check = tk.Radiobutton(
            frame,
            variable=weeks,
            text='1 week',
            value=1,
            command=option_changed_week(weeks.get()))
        weeks_check.grid(column=3, row=2, sticky=tk.W)
        weeks_check.config(bg="#191919", fg="#cbcbcb",
                           selectcolor="#191919",
                           font=("Calibri", 20),
                           activebackground="#191919",
                           activeforeground="#cbcbcb")
        weeks_check = tk.Radiobutton(frame,
                                    variable=weeks,
                                    text='2 weeks',
                                    value=2,
                                    command=option_changed_week(weeks.get()))
        weeks_check.grid(column=3, row=3, sticky=tk.W)
        weeks_check.config(bg="#191919", fg="#cbcbcb",
                    selectcolor="#191919",
                    font=("Calibri", 20),
                    activebackground="#191919",
                    activeforeground="#cbcbcb")
        weeks_check = tk.Radiobutton(frame,
                                    variable=weeks,
                                    text='3 weeks',
                                    value=3,
                                    command=option_changed_week(weeks.get()))
        weeks_check.grid(column=3, row=4, sticky=tk.W)
        weeks_check.config(bg="#191919", fg="#cbcbcb",
                    selectcolor="#191919",
                    font=("Calibri", 20),
                    activebackground="#191919",
                    activeforeground="#cbcbcb")
        weeks_check = tk.Radiobutton(frame,
                                    variable=weeks,
                                    text='4 weeks',
                                    value=4,
                                    command=option_changed_week(weeks.get()))
        weeks_check.grid(column=3, row=5, sticky=tk.W)
        weeks_check.config(bg="#191919", fg="#cbcbcb",
                    selectcolor="#191919",
                    font=("Calibri", 20),
                    activebackground="#191919",
                    activeforeground="#cbcbcb")

        for widget in frame.winfo_children():
            widget.grid(padx=5, pady=5)

        return weights, weeks
    else:
        options = False
        hide_frame(frame)

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
    
def is_confirmed():
    global confirm
    confirm = True

def is_options():
    global options
    options = False
    
###############################################################################
# RECIPES #####################################################################
###############################################################################

def create_recipes_frame(container):
    global weeks
    frame = tk.Frame(container,
                    bg="#191919",
                    width=790,
                    height=490, bd=0)
    
    frame_menu = tk.Frame(container,
            bg="#1d1947",
            width=75,
            height=505)
    
    frame_buttons = tk.Frame(frame_menu,
                bg="#1d1947")

    
    # grid layout for the recipes frame
    # frame.columnconfigure(0, weight=1)
    # frame.columnconfigure(0, weight=3)
    frame.place(x=100, y=10)
    frame_buttons.place(x=10, y=10)
    frame_menu.place(x=15, y=10)
    
    # Weeks
    for i in range(4):
        tk.Label(frame,
                 text='Tydzień {0}:'.format(i),
                 bg="#191919", fg="#cbcbcb",
                 font=("Calibri", 20)).grid(column=0, row=i, sticky=tk.W)
        button = tk.Button(frame,
                           text='PRZEPISY'.format(i),
                           font=("Calibri", 20),
                           bg="#333241", fg="#cbcbcb",
                           activebackground="#333241",
                           activeforeground="#cbcbcb")
        button.grid(column=1, row=i, sticky=tk.W)
        
    # Menu
    menu_button = tk.Button(frame_buttons,
                            text='Menu')
    menu_button.grid(column=0, row=0)    
    
    graph_button = tk.Button(frame_buttons,
                             text='Graph')
    graph_button.grid(column=0, row=1)
    
    products_button = tk.Button(frame_buttons,
                                text='Products')
    products_button.grid(column=0, row=2)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)
        
    for widget in frame_buttons.winfo_children():
        widget.grid(pady=20)