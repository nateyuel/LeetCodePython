class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        result = float("inf")
        n = len(nums)
        
        for idx in range(n):
            curr = 0

            for idx2 in range(idx, n):
                curr += nums[idx2]
                if l <= idx2 - idx + 1 <= r:
                    if curr > 0:
                        result = min(result, curr)
        
        return result if result != float("inf") else -1