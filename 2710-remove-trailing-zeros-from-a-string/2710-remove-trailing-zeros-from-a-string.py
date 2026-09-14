class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        zero_count = 0
        n = len(num)

        for i in range(n-1, -1, -1):
            if num[i] != "0":
                break
            else:
                zero_count += 1
        
        return num[:n-zero_count]