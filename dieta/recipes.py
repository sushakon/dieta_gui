import tkinter as tk
from tkinter import TclError, ttk
from options import weeks

def hide_frame(frame):
    frame.destroy()

def create_recipes_frame(container):
    global weeks
    menu_img = tk.PhotoImage(file="button5.png")
    menu_back = tk.PhotoImage(file="back.png")
    
    #frames
    frame_weeks = tk.Frame(container,
                     bg="#191919",
                     width=680,
                     height=505)
    
    frame_menu = tk.Frame(container,
                         bg="#1d1947",
                         width=75,
                         height=505)
    
    frame_buttons = tk.Frame(frame_menu,
                bg="#1d1947")
    
    frame_week_1 =  tk.Frame(frame_weeks,
                bg="#191919")
    
    frame_week_2 =  tk.Frame(frame_weeks,
                bg="#191919")
    
    frame_week_3 =  tk.Frame(frame_weeks,
                bg="#191919")
    
    frame_week_4 =  tk.Frame(frame_weeks,
                bg="#191919")
    
    # grid layout for the recipes frame
    frame_buttons.place(x=18, y=10)
    frame_menu.place(x=15, y=10)
    frame_weeks.place(x=105, y=10)
    frame_week_1.place(x=20, y=20)
    frame_week_2.place(x=20, y=140)
    frame_week_3.place(x=20, y=260)
    frame_week_4.place(x=20, y=380)
    
    # Weeks  
    sep1 = ttk.Separator(frame_weeks, orient='horizontal')
    sep1.place(x=10, y=10, width=660)
    
    label_week_1 = tk.Label(frame_week_1,
                            text='Tydzień I:',
                            bg="#191919", fg="#cbcbcb",
                            font=("Calibri", 20))
    label_week_1.grid(column=0, row=0, sticky=tk.W)
    recipes_week_1 =  tk.Button(frame_week_1,
                                text='PRZEPISY',
                                font=("Calibri", 20),
                                width=45,
                                bg="#333241", fg="#cbcbcb",
                                activebackground="#333241",
                                activeforeground="#cbcbcb")
    recipes_week_1.grid(column=0, row=1, sticky=tk.W)
    
    sep2 = ttk.Separator(frame_weeks, orient='horizontal')
    sep2.place(x=10, y=135, width=660)
    
    label_week_2 = tk.Label(frame_week_2,
                            text='Tydzień II:',
                            bg="#191919", fg="#cbcbcb",
                            font=("Calibri", 20))
    label_week_2.grid(column=0, row=0, sticky=tk.W)
    recipes_week_2 =  tk.Button(frame_week_2,
                                text='PRZEPISY',
                                font=("Calibri", 20),
                                width=45,
                                bg="#333241", fg="#cbcbcb",
                                activebackground="#333241",
                                activeforeground="#cbcbcb")
    recipes_week_2.grid(column=0, row=1, sticky=tk.W)
    
    sep3 = ttk.Separator(frame_weeks, orient='horizontal')
    sep3.place(x=10, y=255, width=660)
    
    label_week_3 = tk.Label(frame_week_3,
                            text='Tydzień III:',
                            bg="#191919", fg="#cbcbcb",
                            font=("Calibri", 20))
    label_week_3.grid(column=0, row=0, sticky=tk.W)
    recipes_week_3 =  tk.Button(frame_week_3,
                                text='PRZEPISY',
                                font=("Calibri", 20),
                                width=45,
                                bg="#333241", fg="#cbcbcb",
                                activebackground="#333241",
                                activeforeground="#cbcbcb")
    recipes_week_3.grid(column=0, row=1, sticky=tk.W)
    
    sep4 = ttk.Separator(frame_weeks, orient='horizontal')
    sep4.place(x=10, y=375, width=660)
    
    label_week_4 = tk.Label(frame_week_4,
                            text='Tydzień II:',
                            bg="#191919", fg="#cbcbcb",
                            font=("Calibri", 20))
    label_week_4.grid(column=0, row=0, sticky=tk.W)
    recipes_week_4 =  tk.Button(frame_week_4,
                                text='PRZEPISY',
                                font=("Calibri", 20),
                                width=45,
                                bg="#333241", fg="#cbcbcb",
                                activebackground="#333241",
                                activeforeground="#cbcbcb")
    recipes_week_4.grid(column=0, row=1, sticky=tk.W)
    
    sep5 = ttk.Separator(frame_weeks, orient='horizontal')
    sep5.place(x=10, y=495, width=660)
        
    # Menu
    menu_button = tk.Button(frame_buttons,
                            image=menu_img,
                            bg="#1d1947",
                            # compound="center",
                            borderwidth=0,
                            highlightthickness=0,
                            activebackground="#1d1947",
                            padx=0, pady=0,
                            command= lambda: menu_more(container, menu_back))
    menu_button.image = menu_img
    menu_button.grid(column=0, row=0)    
           
    # for widget in frame_week_1.winfo_children():
    #     widget.grid(padx=5, pady=5)
        
    for widget in frame_buttons.winfo_children():
        widget.grid(pady=20)
        
        
def menu_more(frame, im):
    frame_menu_options = tk.Frame(frame,
                                  bg="#1d1947",
                                  width=75,
                                  height=500)
    frame_menu_options.place(x=15, y=10)
    
    frame_buttons = tk.Frame(frame_menu_options,
                             bg="#1d1947")
    frame_buttons.place(x=8, y=0)
    
    # go_back_button = tk.Button(frame_buttons,
    #                         text='BACK',
    #                         command= lambda: hide_more())
    # go_back_button.grid(column=0, row=0)  
    
    go_back_button = tk.Button(frame_buttons,
                        image=im,
                        bg="#1d1947",
                        # compound="center",
                        borderwidth=0,
                        activebackground="#1d1947",
                        highlightthickness=0,
                        padx=0, pady=0,
                        command= lambda: hide_more())
    go_back_button.image = im
    go_back_button.grid(column=0, row=0)   
    
    graph_button = tk.Button(frame_buttons,
                             text='Graph')
    graph_button.grid(column=0, row=1)
    
    products_button = tk.Button(frame_buttons,
                                text='Products')
    products_button.grid(column=0, row=2)
    
    for widget in frame_buttons.winfo_children():
        widget.grid(pady=25)

    def hide_more():
        frame_menu_options.destroy()