class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max_k = 0
        idx = 0
        n = len(sequence)
        m = len(word)

        for idx in range(n):
            for idx2 in range(idx + m - 1, n):
                if (idx2 - idx + 1) % m == 0:
                    t = (idx2 - idx + 1) // m
                    if sequence[idx : idx2 + 1] == word * t:
                        max_k = max(max_k, t)
        
        return max_k
