# define the Item Class

class Item:

    def __init__(self, name, desc, room_name, use_desc, room_desc, exit):
        self._name = name #item name
        self._description = desc #item description when looked at
        self._room_name = room_name #name of room item is used in
        self._use_desc = use_desc #description of item use to display to user
        self._room_desc = room_desc #number of room description to use after item use
        self._exit = exit #direction unlocked by item use

    def toDict(self):
        d = {}
        d['name'] = self._name
        d['description'] = self._description
        return d

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def use(self, room):
        if self._room_name == "None":
            return {"use description": self._use_desc, "room description": self._room_desc, "exit": self._exit}
        elif room == self._room_name:
            return {"use description": self._use_desc, "room description": self._room_desc, "exit": self._exit}
        else:
            return -1
        pass
