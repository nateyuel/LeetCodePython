class Solution:
    def largestOddNumber(self, num: str) -> str:
        last_idx = -1

        for idx, x in enumerate(num):
            if int(x) % 2:
                last_idx = idx
        
        return num[:last_idx + 1] if last_idx != -1 else ""

        