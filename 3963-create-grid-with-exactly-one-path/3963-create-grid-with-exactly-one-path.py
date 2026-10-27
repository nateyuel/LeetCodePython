class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        result = []

        for r in range(m):
            temp = ""
            for c in range(n):
                if c == 0 or r == m - 1:
                    temp += "."
                else:
                    temp += "#"
            
            result.append(temp)
        
        return result 
