import json
from datetime import time, datetime
import psutil

class GameTimeSystem:
    DATA = {}
    GAME_DATA = {}
    USER = {}
    GAMES = {}
    MAX_PLAYTIME = 0



    def is_game_process_running(game):
        """
        Check if a certain game is within active processes.
        """
        for process in psutil.process_iter(['name']):
            if game == process.info['name']:
                return True
        return False

    @classmethod
    def main(cls):
        games = cls.GAMES  # Add your actual game process names here
        current_game = None
        start_time = None

        while True:
            if current_game:
                if not cls.is_game_process_running(current_game):
                    cls.update_play_time(current_game, time.time() - start_time)
                    print(f"{current_game} stopped.")
                    current_game = None
                else:
                    print(f"{current_game} is still running.")
            else:
                for game in games:
                    if cls.is_game_process_running(game):
                        current_game = game
                        start_time = time.time()
                        print(f"{current_game} started.")
                        break

            datetime.time.sleep(300)  # check every 5 minutes



    @classmethod
    def load_data(cls):
        with open('../Data/UserData.Json', 'r') as file:
            cls.DATA = json.load(file)
            cls.USER = cls.DATA["user"]
            cls.MAX_PLAYTIME = cls.USER["daily-time-limit"]
        with open('../Data/GameData.Json', 'r') as file:
            cls.GAME_DATA = json.load(file)
            cls.GAMES = list(map(lambda x: x['GameName'], cls.GAME_DATA))

    @classmethod
    def save_data(cls):
        with open('../Data/UserData.Json', 'w') as file:
            json.dump(cls.DATA, file)

    @classmethod
    def update_play_time(cls, game_name, play_time):
        # Call load-data to be sure we have the latest data
        cls.load_data()
        for game in cls.USER['games']:
            if game['GameName'] == game_name:
                game_time = game["TimePlayed"]
                game_time['today'] += play_time
                game_time['this_month'] += play_time
        # saving data after updating
        cls.save_data()

    @classmethod
    def get_game_data(cls):
        # Call load-data to be sure we have the latest data
        cls.load_data()
        return cls.USER['games']

    @classmethod
    def get_daily_play_time(cls):
        # Call load-data to be sure we have the latest data
        cls.load_data()
        return sum(game['TimePlayed']['today'] for game in cls.USER['games'])

    @classmethod
    def get_monthly_play_time(cls):
        # Call load-data to be sure we have the latest data
        cls.load_data()
        return sum(game['TimePlayed']['this_month'] for game in cls.USER['games'])


# Load data the first time the module is loaded
GameTimeSystem.load_data()
