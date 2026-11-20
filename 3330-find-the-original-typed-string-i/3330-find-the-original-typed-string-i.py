class Solution:
    def possibleStringCount(self, word: str) -> int:
        prev = word[0]
        result = 1
        n = len(word)

        for idx in range(1, n):
            if word[idx] == prev:
                result += 1
            prev = word[idx]

        return result
