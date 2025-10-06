# With Numpy array
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[0,1])  #returns 2


# With List:
arr2d = [
    [1, 2, 3],
    [4, 5, 6]
]

print(arr2d[0][1]) # returns 2


# With a wrapper class:
class Matrix:
    def __init__(self, data):
        self.data = data
    def __getitem__(self, indices):
        i, j = indices
        return self.data[i][j]

arr = Matrix([[1,2,3],[4,5,6]])
print(arr[0,1])  # returns 2



