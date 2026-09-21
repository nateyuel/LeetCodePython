class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [0] * k

        dp = [0] * k
        for idx in range(n):
            rolling_arr = [0] * k
            rolling_arr[nums[idx] % k] += 1

            for r in range(k):
                rolling_arr[(r * nums[idx]) % k] += dp[r]
            
            dp = rolling_arr

            for r in range(k):
                result[r] += dp[r]
        
        return result