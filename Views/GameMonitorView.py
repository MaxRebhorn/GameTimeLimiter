import customtkinter as ctk
from tkinter import simpledialog,ttk
from Systems.GameMonitorSystem import GameMonitorSystem


class GameMonitorView(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        self.title("Game Monitor")
        self.geometry("800x600")
        self.create_widgets()

    def add_game(self):
        game_name = simpledialog.askstring("Input", "Enter the name of the game's executable:")
        if game_name is not None:
            GameMonitorSystem.add_game(game_name)

    def update_games(self):
        # Clear all current items in the tree
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Insert updated data into the treeview
        games = GameMonitorSystem.get_games()
        if games is not None:
            for game in games:
                self.tree.insert("", "end", text=game['GameName'],
                                 values=(game['TimePlayed']['today'],
                                         game['TimePlayed']['current_session'],
                                         game['TimePlayed']['this_month'],
                                         game['StartDate'],
                                         game['LastPlayed']))

        # Call this method again after 1000ms (1 second)
        self.after(1000, self.update_games)

    def create_widgets(self):
        # code to draw GUI
        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("name", "today", "current_session", "this_month", "start_date", "last_played")
        self.tree.column("name", width=100)
        self.tree.column("today", width=100)
        self.tree.column("current_session", width=100)
        self.tree.column("this_month", width=100)
        self.tree.column("start_date", width=100)
        self.tree.column("last_played", width=100)
        self.tree.heading("name", text="Game Name")
        self.tree.heading("today", text="Playtime Today")
        self.tree.heading("current_session", text="Current Session")
        self.tree.heading("this_month", text="Playtime This Month")
        self.tree.heading("start_date", text="Start Date")
        self.tree.heading("last_played", text="Last Played")

        self.add_game_button = ctk.CTkButton(self, text="Add Game", command=self.add_game)
        self.add_game_button.place(rely=1.0, relx=1.0, x=0, y=0, anchor="se")

        self.tree.pack()
        self.update_games()  # Start updating games


if __name__ == "__main__":
    app = GameMonitorView()
    app.mainloop()

