class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        comp_sum = 0

        for x in range(1, n + k + 1):
            if abs(n - x) <= k and (n & x) == 0:
                comp_sum += x
        
        return comp_sum