class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        mid = nums[n // 2]
        return sum(abs(mid - num) for num in nums)