from random import randrange
from utilities import Singleton


@Singleton
class Board(object):
    """ board representation. it is a list-like object
        __repr__ needs to be implemented, so that
        calling:
        
        >>> b = Board()
        >>> print b
        
        would print nice board representation.
        there is only one instance of Board as it is a Singleton.
        list syntax can be used:

        >>> b[0]

        would return self.board[0].
        methods __getslice__ and __setslice__ should be implemented
        
        """
    def __init__(self):
        self.board = []
        self.finished = []

    def __repr__(self):
        """ should return a string representing the board.
            for now it only prints the board and returs empty string.
            to be reimplemented!
        """
        reprs = { 0: '.',
                  1:'W',
                 -1:'b' }
        print '\nCURRENT BOARD: '
        for x in range(30):
            if x % 10 == 0:
                print '\n'
            field = reprs[self.board[x]]
            if x in [25,27,28] and self.board[x] == 0:
                field = '*'
            if x == 26:
                field = '~'
            print  '   ', field,
        print '\n'
        return ''
   
    def __getitem__(self, n):
        """ return field n """
        return self.board[n]

    def __setitem__(self, n, v):
        """ change field n on a current board into a v value """
        self.board[n] = v

