class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        result = 0

        for word in sentences:
            result = max(result, len(word.split(" ")))
        
        return result 