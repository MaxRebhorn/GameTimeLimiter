import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image
from Systems.GameMonitorSystem import GameMonitorSystem
import extract_icon


class AddGameDialog(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.title("Add Game")

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Select Game Exe").grid(row=0, column=0, sticky='w')

        self.exe_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.exe_var).grid(row=0, column=1)

        ttk.Button(self, text="Browse", command=self.browse_exes).grid(row=0, column=2)

        ttk.Button(self, text="Add Game", command=self.add_game).grid(row=1, column=0, columnspan=3)

    def browse_exes(self):
        filename = filedialog.askopenfilename(filetypes=[('Executable files', '*.exe')])
        if filename:
            self.exe_var.set(filename)

    def add_game(self):
        GameMonitorSystem.add_game(self.exe_var.get())
        self.destroy()
