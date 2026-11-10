class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        result = 0
        n = len(words)

        for idx in range(n - 1):
            for idx2 in range(idx + 1, n):
                if words[idx2] and words[idx] == words[idx2][::-1]:
                    result += 1
                    words[idx2] = ""
        
        return result 