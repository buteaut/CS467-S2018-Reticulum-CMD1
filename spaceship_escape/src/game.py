# File: game.py
# Author: Reticulum Team
# Date: 4-19-18
# Description: This is the file where the game class is defined.

import platform, os
from RoomClass import Room
from FileEngine import FileReader
from FileEngine import GameSaver
from ItemClass import Item
from ParserClass import Parser
import textwrap

class Game:
    def __init__(self):
        self.inventory = {}
        self.map = {"00":{"name":"Void"}, "01":{"name": "Void"}, "02":{"name": "Void"}, "03":{"name": "Void"}, "04":{"name": "Void"}, "05":{"name": "Space", "description": 0, "inventory": {}, "exits": {}, "exit_locks": {}}, "06":{"name": "Space Near Escape Pod", "description": 0, "inventory": {}, "exits": {}, "exit_locks": {}},
                       "10":{"name":"Void"}, "11":{"name": "Virtual Reality Chamber", "description": 0, "inventory": {}, "exits": {}, "exit_locks": {}}, "12":{"name": "Void"}, "13":{"name": "Void"}, "14":{"name": "Plant Lab", "description": 0, "inventory": {}, "exits": {}, "exit_locks": {}}, "15":{"name": "Space Near EVA Chamber", "description": 0, "inventory": {}, "exits": {}, "exit_locks": {}}, "16":{"name": "Escape Pod", "description": 0, "inventory": {}, "exits": {}, "exit_locks": {}},
                       "20":{"name": "Crew Sleeping Quarters", "description": 0, "inventory": {}, "exits": {}, "exit_locks": {}}, "21":{"name": "Mess Hall", "description": 0, "inventory": {}, "exits": {}, "exit_locks": {}}, "22":{"name": "Busy Hallway", "description": 0, "inventory": {}, "exits": {}, "exit_locks": {}}, "23":{"name": "Station Control Room", "description": 0, "inventory": {}, "exits": {}, "exit_locks": {}}, "24":{"name": "Energy Generation Plant", "description": 0, "inventory": {}, "exits": {}, "exit_locks": {}}, "25":{"name": "EVA Prep Chamber", "description": 0, "inventory": {}, "exits": {}, "exit_locks": {}}, "26":{"name": "Loading Dock", "description": 0, "inventory": {}, "exits": {}, "exit_locks": {}},
                       "30":{"name":"Void"}, "31":{"name": "Holding Chamber", "description": 0, "inventory": {}, "exits": {}, "exit_locks": {}}, "32":{"name":"Void"}, "33":{"name": "Navigation Control Room", "description": 0, "inventory": {}, "exits": {}, "exit_locks": {}}, "34":{"name":"Void"}, "35":{"name":"Void"}, "36":{"name": "Maintenance Room", "description": 0, "inventory": {}, "exits": {}, "exit_locks": {}}}  # 7x4 array of rooms
        self.end_flag = {"rations":False, "map":False}
        self.xCoord = 0  # x-coordinate for map array
        self.yCoord = 0  # y-coordinate for map array
        self.current_room = None
        self.rooms = FileReader()
        self.roomDict = self.rooms.getRoomsFromFiles()
        # dictionary maps verbs to associated functions
        self.actions = {
            'new game': self.startup,
            'look': self.look,
            'help': self.help,
            'inventory': self.get_inventory,
            'savegame': self.save,
            'save game': self.save,
            'loadgame': self.load,
            'load game': self.load,
            'look at': self.look_at,
            'go': self.travel,
            'take': self.take,
            'pick up': self.take,
            'grab': self.take,
            'use': self.use_item,
            'exit': self.exit_game,
            'walkthrough': self.walkthrough
        }

    def menu(self):
        # prompt player
        print("\nWelcome to Reticulum\n")
        print('What would you like to do?')
        print('New game')
        print('Load game')
        print('Walkthrough')
        print('Exit')
        print('Demo')

        # parse player's input
        command = input('\nType your command: ')
        choice = self.parse(command)

        # helps with testing, DELETE before submitting
        #print('\nKeywords parsed (for demonstration only):')
        #for key in choice:
        #    if choice[key]:
        #        print(key + ': ' + choice[key])
        #print()

        # call method based on parsed verb if one of menu options
        if choice['verb'] in ['new game', 'load game', 'loadgame', 'walkthrough', 'exit']:
            self.actions[choice['verb']]()
        elif choice['verb'] in ['demo']:
            print("# Type a command using one of these verbs ('help', 'take', 'look at', 'inventory', 'walkthrough')")
            print("# Include a noun such as ('rations', 'map', 'key', 'plant', 'suit', 'extinguisher', 'tools', 'clipboard')")
            print("# Include a room such as ('north', 'south', 'east', 'west', 'escape pod', 'loading dock', 'navigation control', 'station control', 'lab', 'energy generation', 'sleeping quarters', 'vr chamber', 'holding chamber')")
            print('# "Exit" ends the loop')
            print("\n# ex. 'Take the plant to the escape pod' or 'LOOKat th loding dock for the kyy' - spelling errors intentional!")

            while(True):
                command = input('\nType a sentence: ')
                choice = self.parse(command)
                if choice['verb'] in ['help', 'take', 'look at', 'inventory', 'walkthrough']:
                    self.actions[choice['verb']](choice)
                elif choice['verb'] in ['exit']:
                    break

    def look(self):
        # get current coordinates and call game_print()
        xy = str(self.xCoord) + str(self.yCoord)
        if len(self.map[xy]['inventory']) == 0:
            items = "A search of the area reveals no obviously useful items."

        else:
            items = "Searching the area for useful items you find "
            for y in self.map[xy]['inventory']:
                items = items + y + ", "

            items = items[0:-2] + "."

        self.game_print(self.map[xy]["description"], None, items)

    def travel(self, input):
        xy = str(self.xCoord) + str(self.yCoord)
        #print(input)
        direction = [0,0]
        travel = None
        if input['room'] is None:
            self.game_print(self.map[xy]["description"],"You stumble around unsure on where to go.")
            return
        elif input['room'] not in ["north", "south", "east", "west", "n", "s", "e", "w"]:
            paths = self.map[xy]["exits"]
            #print("Paths:" + str(paths))
            if 'north' in paths:
                if input['room'] == str.lower(self.map[xy]["exits"]["north"]):
                    travel = "north"
            if "south" in paths:
                if input['room'] == str.lower(self.map[xy]["exits"]["south"]):
                    travel = "south"
            if "west" in paths:
                if input['room'] == str.lower(self.map[xy]["exits"]["west"]):
                    travel = "west"
            if "east" in paths:
                if input['room'] == str.lower(self.map[xy]["exits"]["east"]):
                    travel = "east"
        else:
            travel = input['room']

        if travel is None:
            self.game_print(self.map[xy]["description"], "You stumble around unsure on where to go.")
            return
        else:
            if travel == "north" or travel == "n":
                direction = [-1, 0]
            elif travel == "south" or travel == "s":
                direction = [1, 0]
            elif travel == "west" or travel == "w":
                direction = [0, -1]
            elif travel == "east" or travel == "e":
                direction = [0, 1]
            else:
                self.game_print(self.map[xy]["description"], "You stumble around unsure on where to go.")
                return

        newX = self.xCoord + direction[0]
        newY = self.yCoord + direction[1]
        #print("newX", newX, "newY", newY)
        if(newX > 3 or newX < 0 or newY < 0 or newY > 6):
            print("You cannot travel to the void")
        else:
            xy = str(newX) + str(newY)
            if self.map[xy]["name"] == "Void":
                print("You cannot travel to the void")
            else:
                #print(self.map[xy]["name"])
                self.xCoord = newX
                self.yCoord = newY
                self.load_room(self.map[xy]["name"])
                if self.map[xy]["description"] == 0:
                    self.map[xy]["inventory"] = self.current_room.get_inventory()
                    self.map[xy]["exits"] = self.current_room.get_exit_names()
                    self.map[xy]["exit_locks"] = self.current_room.get_exit_locks()
                    self.map[xy]["description"] = 1
                    self.game_print(0)
                else:
                    self.game_print(self.map[xy]["description"])

    def use_item(self, parsed_tokens):
        #pass
        #if feature key is in parsed_tokens call feature method then handle return statement
        if parsed_tokens['feature'] is not None:
            self.room_feature(parsed_tokens)
        #check if item is in inventory
        elif parsed_tokens['item'] is not None:
            pass
        #if so run item.use() and set event2 equal to the event key from the returned dict
        #if returned dict has an unlock key update that room's exit_locks value
        #if returned dict has a description key update the room's description value
        #game_print(event2)

        #if item not in inventory event2 declares as much

    def room_feature(self, parsed_tokens):
        #pass
        response = self.current_room.feature(parsed_tokens['feature'])
        if response is not -1:
            self.game_print(self.map[str(self.xCoord) + str(self.yCoord)]['description'], None, response)
        else:
            response = "As you go to use %s you feel a wave of confusion. Didn't you see %s somewhere else on the station?" % (parsed_tokens['feature'], parsed_tokens['feature'])
            self.game_print(self.map[str(self.xCoord) + str(self.yCoord)]['description'], None, response)

    def game_loop(self):
        while (True):
            command = input('\nType a sentence: ')
            choice = self.parse(command)
            if choice['verb'] in self.actions:
                if choice['verb'] == 'look':
                    self.look()
                elif choice['verb'] == 'loadgame':
                    self.load()
                else:
                    self.actions[choice['verb']](choice)
            # if no verb simply go to designated room
            elif not choice['verb'] and choice['room']:
                self.actions['go'](choice)


    # parses the verb, item, room, and features from player's input
    # requires a string
    # returns a dictionary of parsed tokens
    def parse(self, command):
        parser = Parser()
        tokens = parser.tokenize(command)
        parsed_tokens = parser.parse_tokens(tokens)

        return parsed_tokens

    def save(self, parsed_tokens):
        save = GameSaver()
        save.saveGame(self)
        self.game_print(self.map[str(self.xCoord) + str(self.yCoord)]["description"], None,"Game saved.")

    def load(self):
        load = GameSaver()
        load.loadGame(self)
        self.game_print(self.map[str(self.xCoord) + str(self.yCoord)]["description"], None, "Game loaded.")
        self.game_loop()

    # format text to taste when testing
    def game_print(self, description, event1 = None, event2 = None):
        # pass
        self.clearscreen()
        #print(self.current_room.get_name())
        # need information on Room class get_exit_names output
        # to make a print statement of the different directions and where they lead
        print(str.center(self.current_room.get_name(), 80, ' '))
        print()
        exitLocks = self.current_room.get_exit_locks()
        exits = self.current_room.get_exit_names()
        exitString = ""
        if "north" in exitLocks and exitLocks["north"] == False:
            exitString = exitString + " North - {} |".format(exits["north"])
        if "south" in exitLocks and exitLocks["south"] == False:
            exitString = exitString + " South - {} |".format(exits["south"])
        if "east" in exitLocks and exitLocks["east"] == False:
            exitString = exitString + " East - {} |".format(exits["east"])
        if "west" in exitLocks and exitLocks["west"] == False:
            exitString = exitString + " West - {} |".format(exits["west"])
        exitString = exitString[0:-1]
        print(str.center(exitString, 80, ' '))
        print()
        if event1 is None and len(self.inventory) > 0:
            event1 = "Your inventory currently contains: "
            for y in self.inventory.keys():
                event1 = event1 + y + ", "
            event1 = event1[0:-2] + "."
        if event1 is not None:
            print(textwrap.fill(event1, 75))
            print()
        if description == 0:
            print(textwrap.fill(self.current_room.get_long(), 75))
            print()
        else:
            self.current_room.set_which_short(description-1)
            print(textwrap.fill(self.current_room.get_short(), 75))
            print()

        if event2 is not None:
            print(event2)
            print()

    def end_game(self):
        pass


    def load_room(self, room):
        self.current_room = self.roomDict[room]

    def clearscreen(self):
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def startup(self):
        self.xCoord = 3
        self.yCoord = 1
        self.load_room(self.map["31"]["name"])
        self.map["31"]["exits"] = self.current_room.get_exit_names()
        self.map["31"]["exit_locks"] = self.current_room.get_exit_locks()
        self.game_print(0)
        self.map["31"]["description"] = 1
        self.game_loop()

    def help(self, parsed_tokens):
        print('\nhelp was called')
        print('this is the dictionary sent with it', parsed_tokens)

    def walkthrough(self, parsed_tokens):
        print('\nwalkthrough was called')
        print('this is the dictionary sent with it', parsed_tokens)

    def get_inventory(self, parsed_tokens):
        print('\nget_inventory was called')
        print('this is the dictionary sent with it', parsed_tokens)

    def look_at(self, parsed_tokens):
        #print('\nlook_at was called')
        #print('this is the dictionary sent with it', parsed_tokens)
        xy = str(self.xCoord) + str(self.yCoord)
        if parsed_tokens['item'] in self.inventory:
            items = "An examination of " + parsed_tokens['item'] + " reveals " + self.inventory[parsed_tokens['item']].get_description()

        elif parsed_tokens['item'] in (self.map[xy]['inventory']):
            items = "An examination of " + parsed_tokens['item'] + " reveals " + self.map[xy]['inventory'][parsed_tokens['item']].get_description()
        else:
            items = "Unable to locate " + parsed_tokens['item'] + " on your person or in the area you visualise what you remember it should be. Unfortunately, your mind wanders to your favorite taco stand back on Earth..."
        self.game_print(self.map[xy]["description"], None, items)

    def take(self, parsed_tokens):
        #print('\ntake was called')
        #print('this is the dictionary sent with it', parsed_tokens)
        player = "You drop the %s." % (parsed_tokens['item'])
        room = "Looking around to see if someone would notice you quickly pocket the %s." % (parsed_tokens['item'])
        missing = "You could have sworn you saw a %s around here but searching both %s and your pockets you can't find it." % (parsed_tokens['item'], self.current_room.get_name())
        if parsed_tokens['item'] in self.inventory.keys():
            i = self.inventory[parsed_tokens['item']]
            name = str(parsed_tokens['item'])
            item = {name: i}
            #print(type(i))
            #print(type(self.map[str(self.xCoord) + str(self.yCoord)]['inventory']))
            #self.map[str(self.xCoord) + str(self.yCoord)]['inventory'].update(item)
            self.map[str(self.xCoord) + str(self.yCoord)]['inventory'][name] = i
            del self.inventory[parsed_tokens['item']]
            self.game_print(self.map[str(self.xCoord) + str(self.yCoord)]['description'], None, player)
        elif parsed_tokens['item'] in self.map[str(self.xCoord) + str(self.yCoord)]['inventory'].keys():
            i = self.map[str(self.xCoord) + str(self.yCoord)]['inventory'][parsed_tokens['item']]
            self.inventory[parsed_tokens['item']] = i
            del self.map[str(self.xCoord) + str(self.yCoord)]['inventory'][parsed_tokens['item']]
            self.game_print(self.map[str(self.xCoord) + str(self.yCoord)]['description'], None, room)
        else:
            self.game_print(self.map[str(self.xCoord) + str(self.yCoord)]['description'], None, missing)


    def exit_game(self, parsed_tokens):
        exit(0)

