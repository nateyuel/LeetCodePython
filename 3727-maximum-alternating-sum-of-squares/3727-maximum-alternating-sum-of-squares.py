class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = [num ** 2 for num in nums]
        squares.sort()
        n = len(squares)
        result = 0

        for idx, sq in enumerate(squares):
            if idx < n // 2:
                result -= sq
            else:
                result += sq
        
        return result