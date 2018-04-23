
# Imports
from actions import *
from rooms import *

# Dictionary that contains verbs for keys and associated functions as values
actions = {}
actions['look'] = look
actions['help'] = get_verbs
actions['inventory'] = get_inventory
actions['save game'] = save_game
actions['load game'] = load_game
actions['look at'] = look_at
actions['go'] = go

# Do action based on input
def do_action(command, Item=None, Room=None):
    actions[command](Item, Room)

# Create room instances
escape_pod = EscapePod()
holding_chamber = HoldingChamber()

# Get user input
command = input('Some action verb: ')
if command == 'look':
    location = input('Name of room: ')

# Call do_action with verb and location
if command == 'look':
    if location == 'escape pod':
        do_action(command, None, escape_pod)
    elif location == 'holding chamber':
        do_action(command, None, holding_chamber)
else:
    do_action(command)