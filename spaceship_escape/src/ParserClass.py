# imports
from itertools import combinations
import string

# general outline for creating parser found here http://textblob.readthedocs.io/en/dev/quickstart.html
class Parser:
    def __init__(self):
        # list of stop words to remove before parsing
        self.stop_letters = list(string.ascii_lowercase)

        # include single letters not related to directions
        for letter in self.stop_letters:
            if letter in ['n', 's', 'e', 'w']:
                self.stop_letters.remove(letter)

        self.stop_words = self.stop_letters + ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']

        # list of words that are relevant to the game
        self.verbs = ['exit', 'look', 'help', 'inventory', 'savegame', 'loadgame', 'save game', 'load game', 'look at', 'go', 'take', 'pick up', 'grab', 'use', 'new game', 'walkthrough', 'demo']
        self.items = ['rations', 'map', 'key', 'plant', 'suit', 'extinguisher', 'tools', 'clipboard']
        self.features = ['door', 'lamp', 'water cooler', 'clamps', 'ship', 'poster', 'footlocker', 'window', 'screens', 'meals', 'seat', 'button', 'paper', 'charts', 'pillars', 'servitor', 'diagram', 'console', 'DRD', 'emptiness', 'lights', 'supplies', 'barrels', 'loader', 'instruments', 'expanse', 'desk']
        self.rooms = ['e', 'w', 's', 'n', 'north', 'south', 'east', 'west', 'escape pod', 'loading dock', 'navigation control', 'station control', 'plant lab', 'energy generation', 'crew sleeping quarters', 'sleeping quarters', 'crew sleeping', 'vr chamber', 'holding chamber', 'maintenance room', 'busy hallway', 'eva prep chamber', 'eva prep', 'prep chamber', 'space near escape pod', 'space near eva chamber', 'mess hall', 'space']
        self.keywords = self.verbs + self.items + self.features + self.rooms

    # parse essential keywords from command
    def tokenize(self, command):
        # check for space near eva chamber and space near escape pod
        discovered_room = []
        for possible_correction in self.edits(command):
            if 'space near eva chamber' in possible_correction:
                discovered_room.append('space near eva chamber')
            elif 'space near escape pod' in possible_correction:
                discovered_room.append('space near escape pod')

        # all single and double words
        single_words = [_ for _ in command.lower().split() if _ not in self.stop_words]
        double_words = [' '.join(word) for word in combinations(single_words, 2)]
        single_and_double_words = double_words + single_words
        all_keywords = discovered_room + single_and_double_words

        # spell correct all tokens with max 1 error
        spell_corrected_tokens = []
        for token in all_keywords:
            if token not in ['e', 'w', 's', 'n']:
                possible_corrections = self.edits(token)
                for possible_correction in possible_corrections:
                    if possible_correction in self.keywords:
                        spell_corrected_tokens.append(possible_correction)
            # single letter directions should never be spell corrected
            elif token in ['e', 'w', 's', 'n']:
                spell_corrected_tokens.append(token)

        return spell_corrected_tokens

    # implementation for following function derived from https://norvig.com/spell-correct.html
    # returns list of all words one error away from target word
    def edits(self, word):
        letters = string.ascii_lowercase + ' '
        word = word.lower()
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]
        return deletes + transposes + replaces + inserts

    # map tokens into different types of keywords
    def parse_tokens(self, tokens):
        # mapped keywords
        parsed_tokens = {
            'verb': None,
            'item': None,
            'feature': None,
            'room': None
        }

        # convert two-word names to three-word names
        room_names = {
            'navigation control': 'navigation control room',
            'station control': 'station control room',
            'energy generation': 'energy generation plant',
            'sleeping quarters': 'crew sleeping quarters',
            'crew sleeping': 'crew sleeping quarters',
            'prep chamber': 'eva prep chamber',
            'eva prep': 'eva prep chamber',
            'vr chamber': 'virtual reality chamber'
        }

        # find verb, item, feature, location from list of tokens
        for token in tokens:
            if token in self.verbs and not parsed_tokens['verb']:
                parsed_tokens['verb'] = token
            elif token in self.items and not parsed_tokens['item']:
                parsed_tokens['item'] = token
            elif token in self.features and not parsed_tokens['feature']:
                parsed_tokens['feature'] = token
            elif token in self.rooms and not parsed_tokens['room']:
                parsed_tokens['room'] = token
                if parsed_tokens['room'] in room_names:
                    # two-word names to three-word names 
                    parsed_tokens['room'] = room_names[parsed_tokens['room']]

        return parsed_tokens
