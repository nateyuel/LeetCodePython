class Solution:
    def minMoves(self, nums: List[int]) -> int:
        result = 0
        max_num = max(nums)

        for num in nums:
            result += max_num - num
        
        return result 