# Create Room class
class Room:
    def __init__(self):
        self._description = None

    def get_description(self):
        return self._description

# Each room inherits from Room class
class EscapePod(Room):
    def __init__(self):
        self._description = 'inside escape pod:\ngoal is to get here with the necessary items to leave'