import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        import math

        res = [np.round(1 / (1+math.exp(-i)), 5) for i in z]
        return res

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        res = []
        for num in z:
            if num > 0:
                res.append(num)
            else:
                res.append(0.0)

        return res