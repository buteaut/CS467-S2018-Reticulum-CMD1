from RoomClass import Room
from ItemClass import Item
import json
import time

# define the exact file name and path to where the room data is held
class _RoomFileNames:
    _room_names = ["holdingChamber.json"
                   ,"loadingDock.json"
                   ,"navControlRoom.json"
                   ,"stationControlRoom.json"
                   ,"plantLab.json"
                   ,"energyGenPlant.json"
                   ,"crewSleepingQuarters.json"
                   ,"VRChamber.json"
                   ,"escapePod.json"
                   ,"maintenanceRoom.json"
                   ,"busyHallway.json"
                   ,"EVAPrepChamber.json"
                   ,"spaceNearEscapePod.json"
                   ,"spaceNearEVAChamber.json"
                   ,"messHall.json"
                   ,"space.json"
                   ]

    _room_files_directory = "../room_data/"

# define path and filenames for saved games
class _GameFileNames:
    _game_files_directory = "../saved_games/"
    _saved_game_filename = "game.json"

class GameSaver:
    # save to current state of the game to a JSON encoded data file
    def saveGame(self, game):
        # gameDict will be written as json to file
        gameDict = {}

        # load data fields from current state of game
        # into these tmp variables
        gameInventory = game.inventory
        gameMap = game.map
        gameEndFlag = game.end_flag
        gameXCoord = game.xCoord
        gameYCoord = game.yCoord
        gameCurrentRoom = game.current_room.toDict()

        # create the gameDict as a pseudo game object
        gameDict['inventory'] = gameInventory
        gameDict['map'] = gameMap
        gameDict['end_flag'] = gameEndFlag
        gameDict['xCoord'] = gameXCoord
        gameDict['yCoord'] = gameYCoord
        gameDict['current_room'] = gameCurrentRoom

        # add another field 'time' to track when this current game
        # was saved
        gameDict['timeSaved'] = time.time()

        f = open(_GameFileNames._game_files_directory
                 + _GameFileNames._saved_game_filename,
                 "w")

        f.write(json.dumps(gameDict))
        f.close()

    # read from a JSON encoded file containing the state of a game when
    # it was saved. Set the data fields of the passed in Game object
    # to the values contained in the data file
    def loadGame(self, game):
        try:
            f = open(_GameFileNames._game_files_directory
                     + _GameFileNames._saved_game_filename,
                     "r")
        except OSError:
            print("No Saved Game File To Load")
            return

        gameDict = json.loads(f.read())
        f.close()

        gameInventory = gameDict['inventory']
        gameMap = gameDict['map']
        gameEndFlag = gameDict['end_flag']
        gameXCoord = gameDict['xCoord']
        gameYCoord = gameDict['yCoord']

        currRoom = gameDict['current_room']
        currRoomInven = []
        for i in range(0, len(currRoom['inventory'])):
            currRoomInven.append(Item(currRoom["inventory"][i]["name"],
                                      currRoom["inventory"][i]["description"]))

        gameCurrentRoom = Room(currRoom['name'],
                               currRoom['long'],
                               currRoom['short'],
                               currRoom['which_short'],
                               currRoomInven,
                               currRoom['exits'],
                               currRoom['locks'],
                               currRoom['feature1keys'],
                               currRoom['feature2keys'],
                               currRoom['examinable_objects'])

        game.inventory = gameInventory
        game.map = gameMap
        game.end_flag = gameEndFlag
        game.xCoord = gameXCoord
        game.yCoord = gameYCoord
        game.current_room = gameCurrentRoom

# FileReader has one method 'getRoomsFromFiles' which will return
# a dictionary of Room objects with each key being the full name of the Room.
# This class will search for Room files based on the parameters defined in the
# internal class _RoomFileNames. Any change made to the names and or directory
# structure of the Room data files must be reflected in the _RoomFileNames class
class FileReader:
    def getRoomsFromFiles(self):
        rooms_dict = {}
        for fname in _RoomFileNames._room_names:
            f = open(_RoomFileNames._room_files_directory + fname, "r")
            pyDict = json.loads(f.read())

            # create a new Item for each item in inventory_list
            inventory_list = {}
            for i in range(0, len(pyDict["inventory_list"])):
                key =(pyDict["inventory_list"][i]['name'])
                #print("key:" + key)
                inventory_list[key] = (Item(pyDict["inventory_list"][i]["name"], pyDict["inventory_list"][i]["description"],
                                            pyDict["inventory_list"][i]["room_name"], pyDict["inventory_list"][i]["use_desc"],
                                            pyDict["inventory_list"][i]["room_desc"], pyDict["inventory_list"][i]["exit"]))
                #print(inventory_list[key]._room_name)
                #print(inventory_list[key].keys())
            # create the Room object
            newRoom = Room(pyDict["room_name"],
                           pyDict["long_description"],
                           pyDict["short_description"],
                           pyDict["which_short"],
                           inventory_list,
                           pyDict["exit_names"],
                           pyDict["exit_locks"],
                           pyDict["feature1_keywords"],
                           pyDict["feature2_keywords"],
                           pyDict["examinable_objects"])
            #print(newRoom._inventory_list["key"].get_description())
            # add to dict to return
            rooms_dict[newRoom.get_name()] = newRoom
            f.close()

        return rooms_dict
