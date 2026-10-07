class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ""

        for idx, ch in enumerate(s):
            if idx % 2 == 0:
                result += ch
            else:
                result += chr(ord(s[idx-1]) + int(ch))
        
        return result 