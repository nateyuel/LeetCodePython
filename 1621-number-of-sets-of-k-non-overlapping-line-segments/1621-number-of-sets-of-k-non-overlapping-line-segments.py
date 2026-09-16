class Solution:
    MOD = 10**9 + 7
    def numberOfSets(self, n: int, k: int) -> int:
        dp = [1] * n
        prefix_sums = [0] * (n + 1)

        for j in range(n):
            prefix_sums[j + 1] = (prefix_sums[j] + dp[j]) % self.MOD

        for _ in range(k):
            dp[0] = 0
            for j in range(1, n):
                dp[j] = (dp[j - 1] + prefix_sums[j]) % self.MOD
            for j in range(n):
                prefix_sums[j + 1] = (prefix_sums[j] + dp[j]) % self.MOD
                
        return dp[n - 1]