# define the Item Class

class Item:

    def __init__(self, name, desc):
        self._name = name
        self._description = desc

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def use(self):
        pass

