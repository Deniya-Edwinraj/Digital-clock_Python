import tkinter as tk
from tkinter import ttk 

def set_theme(root):
    style = ttk.Style()
    root.configure(bg='#282C34')

    style.theme_use('clam')
    style.configure('TLabel', background='#282C34', foreground='#61AFEF', font=('Helvetica', 48))
    style.configure('TButton', background='#61AFEF', foreground='white', font=('Helvetica', 12), padding=10)
    
    style.map('TButton', background=[('active', '#61AFEF'), ('pressed', '#3B4049')])
