class Solution:
    def minChanges(self, s: str) -> int:
        result = 0
        n = len(s)
        idx = 1

        while idx < n:
            if s[idx] != s[idx - 1]:
                result += 1
            idx += 2

        return result
