from RoomClass import Room
from ItemClass import Item
import json

# define the exact file name and path to where the room data is held
class _RoomFileNames:
    _room_names = ["escapePod.json"
                   ,"loadingDock.json"
                   ,"navControlRoom.json"
                   ,"stationControlRoom.json"
                   ,"plantLab.json"
                   ,"energyGenPlant.json"
                   ,"crewSleepingQuarters.json"
                   ,"VRChamber.json"
                   ,"holdingChamber.json"
                   ,"maintenanceRoom.json"
                   ,"busyHallway.json"
                   ,"EVAPrepChamber.json"
                   ,"spaceNearEscapePod.json"
                   ,"spaceNearEVAChamber.json"
                   ,"messHall.json"
                   ,"space.json"
                   ]

    _room_files_directory = "../room_data/"

# FileReader has one method 'getRoomsFromFiles' which will return
# a dictionary of Room objects with each key being the full name of the Room.
# This class will search for Room files based on the parameters defined in the
# internal class _RoomFileNames. Any change made to the names and or directory
# structure of the Room data files must be reflected in the _RoomFileNames class
class FileReader:
    def getRoomsFromFiles():
        rooms_dict = {}
        for fname in _RoomFileNames._room_names:
            f = open(_RoomFileNames._room_files_directory + fname, "r")
            pyDict = json.loads(f.read())

            # create a new Item for each item in inventory_list
            inventory_list = []
            for i in range(0, len(pyDict["inventory_list"])):
                inventory_list.append(Item(pyDict["inventory_list"][i]["name"],
                                           pyDict["inventory_list"][i]["description"]))

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

            # add to dict to return
            rooms_dict[newRoom.get_name()] = newRoom
            f.close()

        return rooms_dict
