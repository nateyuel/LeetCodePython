class Solution:
    def findValidPair(self, s: str) -> str:
        counter = Counter(s)
        n = len(s)

        for idx in range(1, n):
            ch = s[idx]
            prev = s[idx - 1]
            if ch != prev and counter[ch] == int(ch) and counter[prev] == int(prev):
                return prev + ch
        
        return ""