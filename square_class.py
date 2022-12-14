#!/usr/bin/python3
"""square class module"""

class Square:
    """square class"""
    def __init__(self, size):
        """constructor method"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
