# Imports
# from actions import *
from rooms import *
# from spell import *
from itertools import combinations
import string

class Parser:
    def __init__(self):

        # List of stop words to remove before parsing
        self.stop_words = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']

        # List of words that are relevant to the game
        self.verbs = ['exit', 'look', 'help', 'inventory', 'savegame', 'loadgame', 'look at', 'go', 'take', 'pick up', 'grab', 'use', 'new game']
        self.items = ['rations', 'map', 'key', 'plant', 'suit', 'extinguisher', 'tools', 'clipboard']
        self.features = ['door'] # Not complete
        self.rooms = ['north', 'south', 'east', 'west', 'escape pod', 'loading dock', 'navigation control', 'station control', 'lab', 'energy generation', 'sleeping quarters', 'vr chamber', 'holding chamber', 'maintenance', 'hallway', 'prep chamber', 'space near escape pod', 'space near eva chamber', 'mess']
        self.keywords = self.verbs + self.items + self.features + self.rooms

    # Extract essential single and double word commands
    def tokenize(self, command):
        # All single and double words
        single_words = [_ for _ in command.lower().split() if _ not in self.stop_words]
        double_words = [' '.join(word) for word in combinations(single_words, 2)]
        single_and_double_words = double_words + single_words

        # Spell correct all tokens with max 1 error
        spell_corrected_tokens = []
        for token in single_and_double_words:
            possible_corrections = self.edits(token)
            for possible_correction in possible_corrections:
                if possible_correction in self.keywords:
                    spell_corrected_tokens.append(possible_correction)

        return spell_corrected_tokens

    # Implementation for following function derived from https://norvig.com/spell-correct.html
    # Return list of all words similar to target
    def edits(self, word):
        letters = string.ascii_lowercase + ' '
        word = word.lower()
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]
        return deletes + transposes + replaces + inserts

    # # Dictionary that contains verbs for keys and associated functions as values
    # actions = {}
    # actions['new game'] = startup
    # actions['look'] = look
    # actions['help'] = get_verbs
    # actions['inventory'] = get_inventory
    # actions['savegame'] = save_game
    # actions['save game'] = save_game
    # actions['loadgame'] = load_game
    # actions['load game'] = load_game
    # actions['look at'] = look_at
    # actions['go'] = go
    # actions['take'] = take
    # actions['pick up'] = take
    # actions['grab'] = take
    # actions['use'] = use

    # Do action based on input
    def do_action(self, command, Item=None, Room=None, Feature=None):
        actions[command](Item, Room, Feature)


    # # Parser - Continue running until command 'exit'
    # while True:
    #     # Get user input
    #     command = input('\ntype a command: ')

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
            exit(0)
        elif verb:
            do_action(verb, item, escape_pod, feature)
        else:
            print('command not recognized')
