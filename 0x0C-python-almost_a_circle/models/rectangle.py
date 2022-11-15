#!/usr/bin/python3
"""Module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle used to define a rectangle
    ...
    Attributes
    ----------
    width : int
        the width of the rectangle
    height : int
        height of the rectangle
    x : int
        x coordinate
    y : int
        y coordinate
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor to initialize instances"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, val):
        """x setter"""
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, val):
        """y setter"""
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """Return the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """ displays a rectangle """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """ str special method """
        return "[{}] ({}) {}/{} - {}/{}".\
            format(self.__class__.__name__, self.id, self.__x, self.__y,
                   self.__height, self.__width)

    def update(self, *args, **kwargs):
        """Update method"""
        if args is not None and len(args) != 0:
            list_args = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_args[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def to_dictionary(self):
        """Returns the dict representation of the string"""
        return self.__dict__
