import numpy as np
import random

class Board:

    def __init__(self, size: int) -> None:
        self._size = size

        list = [i for i in range(size**2)]
        random.shuffle(list)
        self._list = list
    
    def __str__(self):
        string = ''
        for element in self._list:
            string = string + str(element)
        return (string)
    
    def show(self):
        size = self._size

        matrix = np.array(self._list, dtype=int).reshape((size,size))

        return(matrix)