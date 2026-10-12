class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)

        if n < 3:
            return 0

        result = 0

        for idx in range(n - 2):
            if s[idx] != s[idx + 1] and s[idx] != s[idx + 2] and s[idx + 1] != s[idx + 2]:
                result += 1
        
        return result