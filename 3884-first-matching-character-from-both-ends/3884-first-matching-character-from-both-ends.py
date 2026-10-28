class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)

        for idx, ch in enumerate(s):
            if ch == s[n - idx - 1]:
                return idx

        return -1 