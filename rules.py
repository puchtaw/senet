
class Bell(object):
    """ set of Senet rules by R. C. Bell """
    def __init__(self):
        pass

    def make_move(self):
        pass

    def get_legal_moves(self):
	pass

    def is_legal(self):
	pass


class Kendall(object):
    """ set of senet rules by T. Kendall """
    def __init__(self, board):
        self.b = board

    def new_game(self):
        """ in Kendall`s rules board should have the form:
            board = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        """

        self.b.board = [x for x in [1,-1] * 7] + [0] * 16

    def make_move(self, move):
        """ update board with move.
            move is a tuple returned by Player.play() method
            move = (start, end, player)
        """
        start = move[0]
        end = move[1] if move[1] != 26 else 14
        player = move[2]
        if end > 30:
            self.b[start] = 0
            self.b.finished.append(player)
            return None # break algorithm if piece has finished the race
        
        self.b[start], self.b[end] = self.b[end], self.b[start]            
        
    def is_safe(self, pawn):
        """ return True if pawn is on 26th, 28th or 29th field """
        return True if pawn in [25,27,28] else False

    def is_legal(self, start, end, player):
        """
        A move is ILLIEGAL if:
         (a) b[start] != player        
         (0) b[end] is friendly piece
         (1) b[end] is enemy piece and this piece is connected
           to one or more enemy pieces 
         (2) there are 3 of more concurrent enemy pieces between
             start and end 
         (3) b[end] is enemy piece sitting on safe fields [25, 27, 28]

        """
        # (a):

        
        # (0):

        
        # (1):
        if self.b[end] == -player:
            if self.b[end-1] == -player or self.b[end+1] == -player:
                return False

        # (2): it needs implementing __getslice__() method in Board class
        
        
        # (3):
        return True if not self.is_safe(end) else False


    
    def get_legal_moves(self, throw, player):
        """ return a tuple of all legal moves """
        return ( (0,0,0), (0,0,0) )
