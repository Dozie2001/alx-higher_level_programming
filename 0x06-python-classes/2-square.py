#!/usr/bin/python3
"""The Class of a square"""

class Square:
    """
    Innitialize the size of the square. the size can be specified.
    If they are not, the size defaults to 0
    :param size: int size of square ( > 0)
    """

    def __init__(self,size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
