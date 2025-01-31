import numpy as np
import random

class Board:

    def __init__(self, size: int) -> None:
        self._size = size
        
        numbers = [i for i in range(size**2)]
        random.shuffle(numbers)
        self._numbers = numbers

    @property
    def numbers(self):
        return(self._numbers)

    @numbers.setter
    def numbers(self, new_list: list):
        self._numbers = new_list
    
    def __str__(self):
        string = ''
        for element in self._numbers:
            string = string + str(element)
        return (string)
    
    def show(self):
        size = self._size

        matrix = np.array(self._numbers, dtype=int).reshape((size,size))

        return(matrix)