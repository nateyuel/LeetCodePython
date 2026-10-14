class Solution:
    def minimumMoves(self, s: str) -> int:
        result = 0
        n = len(s)
        idx = 0

        while idx < n:
            if s[idx] == "X":
                result += 1
                idx += 3
            else:
                idx += 1
        
        return result