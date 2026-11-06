class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        result = []
        conc = ""

        for ch in s:
            if len(conc) < k:
                conc += ch
            
            if len(conc) == k:
                result.append(conc)
                conc = ""
        
        if len(conc) > 0:
            result.append(conc + fill * (k - len(conc)))

        return result 