# Associated with 'look' command
# Displays short description of current room
def look(Item, Room):
    print(Room.get_description())

# Associated with 'help' command
# Displays list of available commands
def get_verbs(Item, Room):
    print('These are the available commands:')
    print('look, help, inventory, save game, load game, look at <feature or item>, go <direction or room>, take <item>, use <item>')

# Associated with 'inventory' command
# Displays items in player's inventory
def get_inventory(Item, Room):
    print('This will display list of inventory')

# Associated with 'save game' command
# Saves current game state
def save_game(Item, Room):
    print('This will save game')

# Associated with 'load game' command
# Loads most recently saved game state
def load_game(Item, Room):
    print('This will load game')

# Associated with 'look at' command
# Displays description of specified feature or item
def look_at(Item, Room):
    pass

# Associated with the 'go' command
# Moves player to designated area
def go(Item, Room):
    pass

# Associated with the 'take' command
# Adds item to inventory
def take(Item, Room):
    pass

# Associated with the 'use' command
def use(Item, Room):
    pass