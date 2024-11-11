from datetime import datetime
import json
from os import path


class GameMonitorSystem:
    GAME_DATA_FILE = '../Data/GameData.Json'

    @staticmethod
    def add_game(game_name):
        data = {
            'GameName': game_name,
            'Groups': [],
            'TimePlayed': {
                'today': 0,
                'current_session': 0,
                'this_month': 0
            },
            'StartDate': str(datetime.now()),  # store start date as string
            'LastPlayed': str(datetime.now()),
        }

        game_data = []

        # load the existing data if file exists and is not empty
        if path.exists(GameMonitorSystem.GAME_DATA_FILE) and path.getsize(GameMonitorSystem.GAME_DATA_FILE) > 0:
            with open(GameMonitorSystem.GAME_DATA_FILE, 'r') as file:
                game_data = json.load(file)

        # check if the game is already in the list
        for game in game_data:
            if game['GameName'] == game_name:
                print("This game is already being monitored.")
                return

        # if game is not yet in the list, add it
        game_data.append(data)

        # open the file in write mode and dump the data
        with open(GameMonitorSystem.GAME_DATA_FILE, 'w') as file:
            # write the updated content back to the file
            json.dump(game_data, file, indent=4)

        print("Game added successfully!")

    @staticmethod
    def remove_game(game_name):
        with open(GameMonitorSystem.GAME_DATA_FILE, 'r+') as file:
            game_data = json.load(file)
            game_data = [game for game in game_data if game["GameName"] != game_name]

            # move the pointer to the start of the file
            file.seek(0)

            # write the updated content back to the file
            json.dump(game_data, file, indent=4)

            # truncate any leftover characters
            file.truncate()

        print("Game removed successfully!")

    @staticmethod
    def get_games():
        if not path.exists(GameMonitorSystem.GAME_DATA_FILE) or path.getsize(GameMonitorSystem.GAME_DATA_FILE) == 0:
            return []

        with open(GameMonitorSystem.GAME_DATA_FILE, 'r') as file:
            game_data = json.load(file)

        return game_data

    @staticmethod
    def get_game_groups(game_name):
        with open(GameMonitorSystem.GAME_DATA_FILE, 'r') as file:
            game_data = json.load(file)

        for game in game_data:
            if game["GameName"] == game_name:
                return game["Groups"]

        return None  # return None if no such game found

    @staticmethod
    def add_game_to_group(game_name, group_name):
        with open(GameMonitorSystem.GAME_DATA_FILE, 'r+') as file:
            game_data = json.load(file)

            for game in game_data:
                if game["GameName"] == game_name:
                    game["Groups"].append(group_name)  # add the group name to the game's group list

            # move the pointer to the start of the file
            file.seek(0)

            # write the updated content back to the file
            json.dump(game_data, file, indent=4)

            # truncate any leftover characters
            file.truncate()

        print("Game added to group!")

    @staticmethod
    def remove_game_from_group(game_name, group_name):
        with open(GameMonitorSystem.GAME_DATA_FILE, 'r+') as file:
            game_data = json.load(file)

            for game in game_data:
                if game["GameName"] == game_name and group_name in game["Groups"]:
                    game["Groups"].remove(group_name)  # remove the group name from the game's group list

            # move the pointer to the start of the file
            file.seek(0)

            # write the updated content back to the file
            json.dump(game_data, file, indent=4)

            # truncate any leftover characters
            file.truncate()

        print("Game removed from group!")
