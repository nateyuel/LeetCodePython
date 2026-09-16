class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        result = " " * 1001
        license_counter = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        
        for word in words:
            word_counter = Counter(ch for ch in word if ch.isalpha())
            valid = True
            for ch, freq in license_counter.items():
                if word_counter.get(ch, 0) < freq:
                    valid = False
                    break
            
            if valid and len(word) < len(result):
                result = word
            
        return result 

                
                    

