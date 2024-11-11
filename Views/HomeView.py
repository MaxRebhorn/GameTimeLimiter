import customtkinter as ctk
from tkinter import ttk
from Views import GameMonitorView, GameTimeView


class HomeView(ctk.CTk()):
    def __init__(self, master=None):
        super().__init__(master)
        self.build_buttons()

    def build_buttons(self):
        self.title("Home")

        gamemonitor_button = ttk.Button(self, text="Game Monitor", command=self.load_gamemonitor_view)
        gamemonitor_button.pack(expand=True)

        gametime_button = ttk.Button(self, text="Game Time", command=self.load_gametime_view)
        gametime_button.pack(expand=True)

        # Additional Buttons for future views
        button3 = ttk.Button(self, text="Future View 1", command=self.load_future_view_1)
        button3.pack(expand=True)

        button4 = ttk.Button(self, text="Future View 2", command=self.load_future_view_2)
        button4.pack(expand=True)

    def load_gamemonitor_view(self):
        self.master.destroy()  # Destroy the home view
        root = ctk.CTk()
        gamemonitor_view = GameMonitorView.GameMonitorView(root)
        root.mainloop()

    def load_gametime_view(self):
        self.master.destroy()  # Destroy the home view
        root = ctk.CTk()
        gametime_view = GameTimeView.GameTimeView(root)
        root.mainloop()

    # Implement these functions as the respective views are developed
    def load_future_view_1(self):
        pass

    def load_future_view_2(self):
        pass
