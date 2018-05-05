# Imports
from actions import *
from rooms import *
from spell import *
from itertools import combinations

# List of stop words to remove before parsing
stop_words = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']

# List of words that are relevant to the game
verbs = ['exit', 'look', 'help', 'inventory', 'savegame', 'loadgame', 'look at', 'go', 'take', 'pick up', 'grab', 'use']
items = ['rations', 'map', 'key', 'plant', 'suit', 'extinguisher', 'tools', 'clipboard']
features = ['door'] # Not complete
rooms = ['north', 'south', 'east', 'west', 'escape pod', 'loading dock', 'navigation control', 'station control', 'lab', 'energy generation', 'sleeping quarters', 'vr chamber', 'holding chamber', 'maintenance', 'hallway', 'prep chamber', 'space near escape pod', 'space near eva chamber', 'mess']
keywords = verbs + items + features + rooms

# Extract essential single and double word commands
def tokenize(command):
    # All single and double words
    single_words = [_ for _ in command.lower().split() if _ not in stop_words]
    double_words = [' '.join(word) for word in combinations(single_words, 2)]
    single_and_double_words = double_words + single_words

    # Spell correct all tokens with max 1 error
    spell_corrected_tokens = []
    for token in single_and_double_words:
        possible_corrections = edits(token)
        for possible_correction in possible_corrections:
            if possible_correction in keywords:
                spell_corrected_tokens.append(possible_correction)

    return spell_corrected_tokens

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

# Parser - Continue running until command 'exit'
while True:
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
            # Prevents 'look' from replacing 'look at'
            if not verb:
                verb = token
        elif token in items:
            item = token
        elif token in features:
            feature = token
        elif token in rooms:
            room = token

    # Display metadata
    print('\n' + str(tokens))
    print('verb:', verb)
    print('item:', item)
    print('feature:', feature)
    print('room:', room, '\n')

    # Call do_action with verb and location
    if 'exit' in tokens:
        # Exit loop and end game
        break
    elif verb:
        do_action(verb, item, escape_pod, feature)
    else:
        print('command not recognized')
