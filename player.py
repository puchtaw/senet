from board import Board
from rules import *

class Player(object):
    def __init__(self, name, pl_id, board, rules = Kendall):
        self.name = name # string
        self.pl_id = pl_id # either 1 (white) or -1 (black)
        self.b = board # instance of Board class
        self.rules = rules(self.b) # ruleset

    def play(self, throw):
        """
        player should decide which piece he wants to move.
        return tuple (start, end, pl_id).
        this method should be overriden in machine players.
        """
        start = -1
        end = -1
        while self.b[start]!=self.pl_id :
            print "\nChoose your piece"
            start = int(raw_input("piece to move: "))
    
            end = start + throw
        end = end if end !=27 else 15
        if end > 30:
            return start, end, self.pl_id
        if self.rules.is_legal(start,end,self.pl_id):
            return start, end, self.pl_id
        else:
            return self.play(throw)
        
