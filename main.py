from board import Board
from player import Player
from rules import *
from random import randrange

b = Board()
white = Player("white", 1, b)
black = Player("black",-1, b)
rules = Kendall(b)

class GameOfSenet(object):
    """ this class handles the game, based on rules passed (either Bell or Kendall) """
    def __init__(self, board, white, black, rules):
        
        self.b = board # board is a Singleton instance. see board.py
        self.wh = white # Player() instance. see player.py
        self.bl = black # same
        self.rules = rules # instance of either Bell() or Kendall(). see rules.py
        
        self.to_play = -1 # indicates which player is to move
        self.throw = 0 # holds value of last throw of sticks
        self.players = { 1 : self.wh,
                         -1: self.bl
                         }
        
        self.new_game()

    def new_game(self):
        """ use rules.new_game() to set the new board """
        self.rules.new_game()
        self.new_round()

    def new_round(self):
        """ handle the game """

        # if 1 was thrown player has additional move:
        self.to_play = self.to_play if self.throw in [1,4,5] else -self.to_play
        player = self.players[self.to_play]

        # throw sticks:
        self.sticks()
        print b # prints board representation
        print "    sticks: ", self.throw
        print "    player: ", player.name

        # make a move:
        self.rules.make_move(player.play(self.throw))

        # check wether the game is over and call new_round() again
        if self.game_in_play():
            self.new_round()

    def sticks(self):
        """ simulate throw of sticks """
        face_up = 0
        for x in range(4):
            face_up +=1 if randrange(2)==0 else 0
        self.throw = 5 if face_up == 0 else face_up

    def game_in_play(self):
        """ if game is over return False """
        return False if b.finished.count(self.to_play) == 7 else True

    def get_legal_moves(self):
        return self.rules.get_legal_moves(self.throw, self.to_play)

game = GameOfSenet(b, white, black, rules) # instantiate class
