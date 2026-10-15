class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)

        for idx in range(n):
            dist = set()
            for idx2 in range(idx, n):
                dist.add(nums[idx2])
                result += (len(dist)) ** 2
        
        return result