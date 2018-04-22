# define the Room class here

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

    def feature1(self):
        pass

    def feature1(self):
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

