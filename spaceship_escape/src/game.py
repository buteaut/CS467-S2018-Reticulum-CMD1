# File: game.py
# Author: Reticulum Team
# Date: 4-19-18
# Description: This is the file where the game class is defined.

import platform, os

class Game:
    def __init__(self):
        self.inventory = [None]
        self.map = [[[None],[None],[None],[None],[None],[None],[None]],
                       [[None],[None],[None],[None],[None],[None],[None]],
                       [[None],[None],[None],[None],[None],[None],[None]],
                       [[None],[None],[None],[None],[None],[None],[None]]] #7x4 array of rooms
        self.end_flag = {"rations":False, "map":False}
        self.current_room = None

    def menu(self):
        print("Welcome to Reticulum\n\n")
        print("1) New Game")
        print("2) Load Game")
        print("3) Walkthrough")
        print("4) Exit")

        choice = int(input("Option number:"))
        options = [1, 2, 3, 4]
        while choice not in options:
            print("You choose" + str(choice))
            choice = int(input("Please enter the number of your choice"))

        if choice == 1:
            self.startup()

        elif choice == 2:
            self.load()

        elif choice == 3:
            self.walkthrough()

        else:
            exit(0)

    def move_item(self, item, location_taken, location_put):
        pass

    def look(self, noun):
        pass

    def travel(self, direction):
        pass

    def use_item(self, item, used_with):
        pass

    def parse(self):
        pass

    def save(self):
        pass

    def load(self):
        pass

    def print(self, event1, event2):
        pass

    def end_game(self):
        pass

    def tick(self):
        pass

    def load_room(self, room):
        pass

    def clearscreen(self):
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def startup(self):
        pass

    def help(self):
        pass

    def walkthrough(self):
        pass
