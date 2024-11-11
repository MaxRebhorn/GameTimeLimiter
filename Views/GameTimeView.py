import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Systems.GameMonitorSystem import GameMonitorSystem
import seaborn as sns
import random

class GameTimeView(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Game Time View')
        self.geometry('800x600')
        self._create_widgets()

    def _create_widgets(self):
        # Setting up the layout for the GUI
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create the figure and plotting area
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky='nsew')

    def _update_graph(self):
        # Fetch game data
        games = GameMonitorSystem.get_games()

        # Prepare data for the doughnut chart
        time_data = dict((game['GameName'], game['TimePlayed']['today']) for game in games)

        # Clear the axis for the new plot
        self.ax.clear()

        if time_data:
            # Calculate total playtime and remaining playtime
            total_playtime = sum(time_data.values())
            remaining_playtime = max(0, 2 - total_playtime)  # Assuming max playtime of 24 hours

            # Add remaining time to data
            time_data['Remaining'] = remaining_playtime

            # Get distinct colors for each game, and grey for remaining time
            colors = sns.hls_palette(len(time_data) - 1, l=.5, s=.8).as_hex() + ['#d3d3d3']

            # Create a pie plot
            wedges, text = self.ax.pie(time_data.values(), colors=colors)

            # Create a white circle for the center of the plot to make it a doughnut chart
            centre_circle = plt.Circle((0, 0), 0.70, fc='white')
            fig = plt.gcf()
            fig.gca().add_artist(centre_circle)

            # Add game names as the legend
            self.ax.legend(wedges, time_data.keys(), title="Games", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

            # Add total playtime in the center of the doughnut
            self.ax.text(0, 0, f'Total Playtime\n{total_playtime:.2f}', ha='center', va='center')

            # Redraw the canvas
            self.canvas.draw()

        self.after(1000, self._update_graph)  # Call every second to update graph


if __name__ == "__main__":
    app = GameTimeView()
    app._update_graph()  # Initial call to update graph
    app.mainloop()
