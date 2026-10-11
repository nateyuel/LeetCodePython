class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)

        for idx, num in enumerate(nums):
            if not n % (idx + 1):
                result += num ** 2 

        return result