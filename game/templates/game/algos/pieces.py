# -*- coding: utf-8 -*-

class Position:
    pass

class Piece:
    """
    A chess piece defined by its position
    This is a base class for all types of pieces
    """

    colors = ["white", "black"]

    def __init__(self, position, color):
        self.position = position
        if color not in self.colors:
            raise ValueError
        self.color = color
