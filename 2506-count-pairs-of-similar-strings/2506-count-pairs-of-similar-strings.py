class Solution:
    def similarPairs(self, words: List[str]) -> int:
        counter = defaultdict(int)

        for word in words:
            counter[frozenset(list(word))] += 1
        
        result = 0

        for freq in counter.values():
            if freq > 1:
                result += (freq * (freq - 1)) // 2
        
        return result 
        
