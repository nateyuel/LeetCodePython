class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        result = ""

        for idx in range(n):
            cand = s[idx:]
            if result < cand:
                result = cand

        return result 