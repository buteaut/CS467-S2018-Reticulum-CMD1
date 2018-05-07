import platform, os
from RoomClass import Room
from RoomClass import RoomNames
from FileEngine import FileReader
from FileEngine import GameSaver
from ItemClass import Item
from game import Game

newGame = Game()

gameSaver = GameSaver()
gameSaver.loadGame(newGame)

print(newGame.current_room.get_long())
