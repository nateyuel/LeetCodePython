class Solution:
    def reverseDegree(self, s: str) -> int:
        reverse_degree = 0

        for idx, ch in enumerate(s):
            order = 26 - (ord(ch) - 97)
            reverse_degree += (idx + 1) * order
        
        return reverse_degree