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
        reprs = {-1:'b',
                  0: '_',
                  1:'W'}
        special = {15:'*',
                  25:'!',
                  26:'~',
                  27:'!',
                  28:'!'}
                  

        
                    
        line = '_' * 41
        upper = '|' + '   |'*10
        lower = '%s%s_|'
        bottom = '|' + '___|' * 10

        a = '|'
        b = '|'
        c = '|'
       
        for x in range(10):
            a += lower %('_',reprs[self.board[x]])
        for x in range(19,9, -1):
            frmt = reprs[self.board[x]]
            if self.board != 0:
                frmt = '_', frmt
            else:
                if x not in special:
                    frmt = '_', frmt
                else:
                    frmt = special[x], frmt
            b += lower %(frmt) 
        for x in range(20,30):
            frmt = reprs[self.board[x]]
            if self.board != 0:
                frmt = '_', frmt
            else:
                if x not in special:
                    frmt = '_', frmt
                else:
                    frmt = special[x], frmt
            c += lower %(frmt)

        pattern = '\n  ' + '\n  '.join([
            '   '.join([str(x) for x in range(10)]),
            '  '.join([str(x) for x in range(19,9,-1)]),
            '  '.join([str(x) for x in range(20,30)])
            ]) + '\n'

        
        return '\n'.join([line, upper, a, upper, b, upper, c, pattern])


    
   
    def __getitem__(self, n):
        """ return field n """
        return self.board[n]

    def __setitem__(self, n, v):
        """ change field n on a current board into a v value """
        self.board[n] = v


