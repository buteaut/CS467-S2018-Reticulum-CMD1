# Imports
from itertools import combinations
import string

class Parser:
    def __init__(self):
        # list of stop words to remove before parsing
        self.stop_words = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']

        # list of words that are relevant to the game
        self.verbs = ['exit', 'look', 'help', 'inventory', 'savegame', 'loadgame', 'save game', 'load game', 'look at', 'go', 'take', 'pick up', 'grab', 'use', 'new game', 'walkthrough']
        self.items = ['rations', 'map', 'key', 'plant', 'suit', 'extinguisher', 'tools', 'clipboard']
        self.features = ['door'] # Not complete
        self.rooms = ['north', 'south', 'east', 'west', 'escape pod', 'loading dock', 'navigation control', 'station control', 'lab', 'energy generation', 'sleeping quarters', 'vr chamber', 'holding chamber', 'maintenance', 'hallway', 'prep chamber', 'space near escape pod', 'space near eva chamber', 'mess']
        self.keywords = self.verbs + self.items + self.features + self.rooms

    # parse essential keywords from command
    def tokenize(self, command):
        # All single and double words
        single_words = [_ for _ in command.lower().split() if _ not in self.stop_words]
        double_words = [' '.join(word) for word in combinations(single_words, 2)]
        single_and_double_words = double_words + single_words

        # spell correct all tokens with max 1 error
        spell_corrected_tokens = []
        for token in single_and_double_words:
            possible_corrections = self.edits(token)
            for possible_correction in possible_corrections:
                if possible_correction in self.keywords:
                    spell_corrected_tokens.append(possible_correction)

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

        return parsed_tokens
