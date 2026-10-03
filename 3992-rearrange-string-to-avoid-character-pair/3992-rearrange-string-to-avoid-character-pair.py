class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        result = ""
        count_x = 0

        for ch in s:
            if ch == x:
                count_x += 1
            else:
                result += ch
        
        return result + x * count_x