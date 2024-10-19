import tkinter as tk
from tkinter import ttk
from time import strftime
from theme import set_theme

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title('Digital Clock')
        self.root.geometry('400x200')
        set_theme(self.root)  

        self.time_format_24 = True  
        self.label = ttk.Label(self.root, font=('Helvetica', 48), anchor='center')
        self.label.pack(expand=True)

        self.date_label = ttk.Label(self.root, font=('Helvetica', 16), anchor='center')
        self.date_label.pack(expand=True)

        self.toggle_button = ttk.Button(self.root, text="Switch Format", command=self.toggle_time_format)
        self.toggle_button.pack(side='bottom', pady=10)

        self.update_clock()

    def toggle_time_format(self):
        self.time_format_24 = not self.time_format_24

    def update_clock(self):
        time_format = '%H:%M:%S' if self.time_format_24 else '%I:%M:%S %p'
        current_time = strftime(time_format)
        current_date = strftime('%A, %d %B %Y')

        self.label.config(text=current_time)
        self.date_label.config(text=current_date)

        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalClock(root)
    root.mainloop()
