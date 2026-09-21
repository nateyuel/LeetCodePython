class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        last_idx = 0
        result = [words[0]]

        for idx in range(1, len(words)):
            if groups[last_idx] != groups[idx]:
                result.append(words[idx])
                last_idx = idx
        
        return result
