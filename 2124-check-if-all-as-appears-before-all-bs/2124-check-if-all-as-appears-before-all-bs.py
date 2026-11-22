class Solution:
    def checkString(self, s: str) -> bool:
        curr = s[0]
        n = len(s)

        for idx in range(1, n):
            if curr > s[idx]:
                return False
            else:
                curr = s[idx]
        
        return True