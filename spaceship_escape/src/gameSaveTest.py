import platform, os
from RoomClass import Room
from RoomClass import RoomNames
from FileEngine import FileReader
from FileEngine import GameSaver
from ItemClass import Item
from game import Game

newGame = Game()
newGame.current_room = newGame.roomDict[RoomNames.escapePod]

gameSaver = GameSaver()
gameSaver.saveGame(newGame)
