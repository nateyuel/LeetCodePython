class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        curr_sum = 0
        max_len = -1
        target_sum = sum(nums) - x
        vis = {0:-1}
        
        for idx in range(n):
            curr_sum += nums[idx]

            if curr_sum not in vis:
                vis[curr_sum] = idx
            
            m = curr_sum - target_sum

            if m in vis:
                max_len = max(max_len, idx - vis[m])
        
        return n - max_len if max_len != -1 else -1

