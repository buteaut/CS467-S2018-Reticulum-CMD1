

# Associated with 'look' command
# Displays short description of current room
def look(Item, Room, Feature):
    print(Room.get_description())

# Associated with 'help' command
# Displays list of available commands
def get_verbs(Item, Room, Feature):
    print('These are the available commands:')
    print('look, help, inventory, save game, load game, look at <feature or item>, go <direction or room>, take <item>, use <item>')

# Associated with 'inventory' command
# Displays items in player's inventory
def get_inventory(Item, Room, Feature):
    print('This will display list of inventory')

# Associated with 'save game' command
# Saves current game state
def save_game(Item, Room, Feature):
    print('This will save game')

# Associated with 'load game' command
# Loads most recently saved game state
def load_game(Item, Room, Feature):
    print('This will load game')

# Associated with 'look at' command
# Displays description of specified feature or item
def look_at(Item, Room, Feature):
    if Item:
        print('takes a look at', Item)
    else:
        print('can\'t find that item')

# Associated with the 'go' command
# Moves player to designated area
def go(Item, Room, Feature):
    if not Room:
        print('This will move character to a different room')
    else:
        print('This will move character to', Room.get_name())

# Associated with the 'take' command
# Adds item to inventory
def take(Item, Room, Feature):
    print('This will add item to inventory')

# Associated with the 'use' command
def use(Item, Room, Feature):
    if Item and Feature:
        print('This will use the', Item, 'on the', Feature)
    elif Item:
        print('This will use the', Item)
    else:
        print('You don\'t have that item')
