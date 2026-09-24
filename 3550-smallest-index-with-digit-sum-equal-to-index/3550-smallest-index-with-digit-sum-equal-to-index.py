class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        length = len(nums)
        
        for idx, num in enumerate(nums):
            dig_sum = 0
            while num > 0:
                dig_sum += num % 10
                num //= 10
            
            if dig_sum == idx:
                return idx

        return -1