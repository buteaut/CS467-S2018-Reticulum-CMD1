# define the Room class here

class RoomNames:
    escapePod               = "Escape Pod"
    loadingDock             = "Loading Dock"
    navControlRoom          = "Navigation Control Room"
    stationControlRoom      = "Station Control Room"
    plantLab                = "Plant Lab"
    energyGenPlant          = "Energy Generation Plant"
    crewSleepingQuarters    = "Crew Sleeping Quarters"
    VRChamber               = "Virtual Reality Chamber"
    holdingChamber          = "Holding Chamber"
    maintenanceRoom         = "Maintenance Room"
    busyHallway             = "Busy Hallway"
    EVAPrepChamber          = "EVA Prep Chamber"
    spaceNearEscapePod      = "Space Near Escape Pod"
    spaceNearEVAChamber     = "Space Near EVA Chamber"
    messHall                = "Mess Hall"
    space                   = "Space"

class Room:
    # constructor
    def __init__(self, name, long_desc, short_desc, whichsht, inven, enames,
                 elocks, f1keys, f2keys, objs):
        self._room_name = name
        self._long_description = long_desc
        self._short_description = short_desc
        self._which_short = whichsht
        self._inventory_list = inven
        self._exit_names = enames
        self._exit_locks = elocks
        self._feature1_keywords = f1keys
        self._feature2_keywords = f2keys
        self._examinable_objects = objs

    def toDict(self):
        d = {}
        d['name'] = self._room_name
        d['long'] = self._long_description
        d['short'] = self._short_description
        d['which_short'] = self._which_short
        d['inventory'] = {}
        for i in range(0, len(self._inventory_list)):
            d['inventory'][i.get_name()] = i
        d['exits'] = self._exit_names
        d['locks'] = self._exit_locks
        d['feature1keys'] = self._feature1_keywords
        d['feature2keys'] = self._feature2_keywords
        d['examinable_objects'] = self._examinable_objects
        return d


    def feature1(self):
        pass

    def feature2(self):
        pass

    def get_name(self):
        return self._room_name

    def get_long(self):
        return self._long_description

    def set_which_short(self, which_short):
        self._which_short = which_short

    def get_short(self):
        return self._short_description[self._which_short]

    def get_inventory(self):
        return self._inventory_list

    def add_to_inventory(self, item_to_add):
        pass

    def remove_from_inventory(self, item_to_remove):
        pass

    def get_exit_names(self):
        return self._exit_names

    def get_exit_locks(self):
        return self._exit_locks
