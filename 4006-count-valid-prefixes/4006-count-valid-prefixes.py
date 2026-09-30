class Solution:
    def countValidPrefixes(self, s: str) -> int:
        count_1 = 0
        count_0 = 0
        result = 0

        for ch in s:
            if ch == "1":
                count_1 += 1
            else:
                count_0 += 1
            
            if abs(count_1 - count_0) <= 1:
                result += 1
            
        return result