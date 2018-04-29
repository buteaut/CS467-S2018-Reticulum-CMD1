# File: game.py
# Author: Reticulum Team
# Date: 4-19-18
# Description: This is the file where the game class is defined.

import platform, os
from RoomClass import Room


class Game:
    def __init__(self):
        self.inventory = [None]
        self.map = {"00":{"name":"Void"}, "01":{"name":"Void"}, "02":{"name":"Void"}, "03":{"name":"Void"}, "04":{"name":"Void"}, "05":{"name": "Space", "description": 0, "inventory": []}, "06":{"name": "Space Near Escape Pod", "description": 0, "inventory": []},
                       "10":{"name":"Void"}, "11":{"name": "VR Chamber", "description": 0, "inventory": []}, "12":{"name":"Void"}, "13":{"name":"Void"}, "14":{"name": "Plant Lab", "description": 0, "inventory": []}, "15":{"name": "Space Near EVA Chamber", "description": 0, "inventory": []}, "16":{"name": "Escape Pod", "description": 0, "inventory": []},
                       "20":{"name": "Crew Sleeping Quarters", "description": 0, "inventory": []}, "21":{"name": "Mess Hall", "description": 0, "inventory": []}, "22":{"name": "Busy Hallway", "description": 0, "inventory": []}, "23":{"name": "Station Control Room", "description": 0, "inventory": []}, "24":{"name": "Energy Generation Plant", "description": 0, "inventory": []}, "25":{"name": "EVA Prep Chamber", "description": 0, "inventory": []}, "26":{"name": "Loading Dock", "description": 0, "inventory": []},
                       "30":{"name":"Void"}, "31":{"name": "Holding Chamber", "visited": False, "inventory": [], "short": 0}, "32":{"name":"Void"}, "33":{"name": "Navigation Control Room", "visited": False, "inventory": [], "short": 0}, "34":{"name":"Void"}, "35":{"name":"Void"}, "36":{"name": "Maintenance Room", "visited": False, "inventory": [], "short": 0}}  # 7x4 array of rooms}
        self.end_flag = {"rations":False, "map":False}
        self.xCoord = 0  # x-coordinate for map array
        self.yCoord = 0  # y-coordinate for map array
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
        # pass
        #print("direction 0", direction[0])
        #print("direction 1", direction[1])
        newX = self.xCoord + direction[0]
        newY = self.yCoord + direction[1]
        #print("newX", newX, "newY", newY)
        xy = str(newX) + str(newY)
        des = 0
        if self.map[xy]["name"] == "Void":
            print("You cannot travel to the void")
        else:
            print(self.map[xy]["name"])
            self.xCoord = newX
            self.yCoord = newY
            self.load_room(self.map[xy]["name"])
            if self.map[xy]["description"] == 0:
                self.map[xy]["inventory"] = self.current_room.get_inventory()
                self.map[xy]["description"] = 1
                self.print(0)
            else:
                self.print(self.map[xy]["description"])


    def use_item(self, item, used_with):
        pass

    def parse(self):
        pass

    def save(self):
        pass

    def load(self):
        pass

    #format text to taste when testing
    def print(self, description):
        #pass
        self.clearscreen()
        print(self.current_room.get_name())
        #need information on Room class get_exit_names output
        #to make a print statement of the different directions and where they lead

        if description == 0:
            print(self.current_room.get_long())
        else:
            self.current_room.set_which_short(description-1)
            print(self.current_room.get_short())

    def print(self, description, event1):
        # pass
        self.clearscreen()
        print(self.current_room.get_name())
        # need information on Room class get_exit_names output
        # to make a print statement of the different directions and where they lead
        if description == 0:
            print(self.current_room.get_long())
        else:
            self.current_room.set_which_short(description-1)
            print(self.current_room.get_short())
        print(event1)



    def print(self, description, event1, event2):
        # pass
        self.clearscreen()
        print(self.current_room.get_name())
        # need information on Room class get_exit_names output
        # to make a print statement of the different directions and where they lead

        if description == 0:
            print(self.current_room.get_long())
        else:
            self.current_room.set_which_short(description-1)
            print(self.current_room.get_short())
        print(event1)
        print(event2)

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
