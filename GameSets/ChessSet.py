import abc
from enum import IntEnum

class Board:
    __white_square__ = ''
    __black_square__ = ''
    __side_len__ = 8
    def __init__(self):
        self.board = list()
        for i in range(Board.__side_len__):
            self.board.append([])
            for j in range(Board.__side_len__):
                if  i == 1 or i == 6:
                    self.board[i].append('♙')
                    continue
                if (i + j) % 2 == 0:
                    self.board[i].append(Board.__white_square__)
                else:
                    self.board[i].append(Board.__black_square__)

    def __str__(self):
        lines = '\n'.join((str(i) + '  ' + ''.join(self.board[i][j] for j in range(Board.__side_len__)) for i in range(Board.__side_len__)))
        return lines



class Colours(IntEnum):
    WHITE = 0
    BLACK = 1


class AbstractChessFigure(abc.ABC):
    @abc.abstractmethod
    def __str__(self):
        raise NotImplementedError

    @abc.abstractmethod
    def allowed_moves(self):
        raise NotImplementedError

    @abc.abstractmethod
    def allowed_captures(self):
        raise NotImplementedError

    @abc.abstractmethod
    def colour(self):
        raise NotImplementedError


class Pawn(AbstractChessFigure):
    def __init__(self, colour: int):
        self.colour = colour

if __name__ == '__main__':
    b = Board()
    print(b)