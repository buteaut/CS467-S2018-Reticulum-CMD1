# Create Room class
class Room:
    def __init__(self):
        self._description = None

    def get_description(self):
        return self._description

# Each room inherits from Room class
class EscapePod(Room):
    def __init__(self):
        self._description = 'goal is to get here with the necessary items to leave'

class HoldingChamber(Room):
    def __init__(self):
        self._description = 'where you initially start the game'