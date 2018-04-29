
# Imports
from actions import *
from rooms import *
from itertools import combinations

# List of words that are relevant to the game
verbs = ['exit', 'look', 'help', 'inventory', 'savegame', 'loadgame', 'save game', 'load game', 'look at', 'go', 'take', 'pick up', 'grab', 'use']
items = ['rations', 'map', 'key', 'plant', 'suit', 'extinguisher', 'tools', 'clipboard']
# Feature list not yet determined
features = ['door']
rooms = ['north', 'south', 'east', 'west', 'escape pod', 'loading dock', 'navigation control', 'station control', 'lab', 'energy generation', 'sleeping quarters', 'vr chamber', 'holding chamber', 'maintenance', 'hallway', 'prep chamber', 'space near escape pod', 'space near eva chamber', 'mess']

# Extract essential single and double word commands
def tokenize(command):
    # All single and double words
    single_and_double = [' '.join(word) for word in combinations(command.lower().split(), 2)] + command.lower().split()
    # Find two word combinations that match keywords
    tokens = [word for word in single_and_double if word in verbs or word in items or word in features or word in rooms]
    return tokens

# Dictionary that contains verbs for keys and associated functions as values
actions = {}
actions['look'] = look
actions['help'] = get_verbs
actions['inventory'] = get_inventory
actions['savegame'] = save_game
actions['save game'] = save_game
actions['loadgame'] = load_game
actions['load game'] = load_game
actions['look at'] = look_at
actions['go'] = go
actions['take'] = take
actions['pick up'] = take
actions['grab'] = take
actions['use'] = use

# Do action based on input
def do_action(command, Item=None, Room=None, Feature=None):
    actions[command](Item, Room, Feature)

# Create test room instance
escape_pod = EscapePod()

# Parser
end_game = False

# Continue running until command 'exit'
while not end_game:
    # Get user input
    command = input('\ntype a command: ')

    # Tokenized list of key words from command
    tokens = tokenize(command)

    # Find verb, item, feature, location from list of tokens
    verb = None
    item = None
    feature = None
    room = None

    for token in tokens:
        if token in verbs:
            # Differentitates between 'look' and 'look at'
            if not verb:
                verb = token
        elif token in items:
            item = token
        elif token in features:
            feature = token
        elif token in rooms:
            room = token

    print()
    print(tokens)
    print('verb:', verb)
    print('item:', item)
    print('feature:', feature)
    print('room:', room, '\n')

    # Call do_action with verb and location
    if 'exit' in tokens and len(tokens) == 1:
        end_game = True
    elif verb:
        do_action(verb, item, escape_pod, feature)
    else:
        print('command not recognized')