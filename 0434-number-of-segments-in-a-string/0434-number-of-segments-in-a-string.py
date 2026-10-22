class Solution:
    def countSegments(self, s: str) -> int:
        result = 0
        store = list(s.split(" "))

        for cand in store:
            if cand:
                result += 1
        
        return result 