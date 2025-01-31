import numpy as np

class Board:

    def __init__(self, size: int) -> None:
        self._size = size
    
    def show(self):
        size = self._size

        matrix = [i for i in range(1,size**2 + 1)]
        matrix = np.array(matrix).reshape((size,size))

        return(matrix)