class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:

        ans = init
        for i in range(iterations):

            derivative = 2*ans
            ans -= learning_rate * derivative

        return round(ans, 5)
            
        