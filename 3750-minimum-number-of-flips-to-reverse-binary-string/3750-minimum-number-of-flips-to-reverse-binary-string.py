class Solution:
    def minimumFlips(self, n: int) -> int:
        org = bin(n)[2:]
        reverse = org[::-1]
        result = 0 

        for idx in range(len(org)):
            if org[idx] != reverse[idx]:
                result += 1
        
        return result 