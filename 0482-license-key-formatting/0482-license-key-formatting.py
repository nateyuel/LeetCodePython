class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        n = len(s)
        idx = 0
        s = s[::-1]
        result = ""
        group = ""

        while idx < n:

            if s[idx] != "-":
                group += s[idx].upper()
            
            if len(group) == k and idx < n - 1:
                if len(result) > 0:
                    result += "-" + group
                else:
                    result += group
                group = ""
            elif idx == n - 1 and len(group) > 0:
                if len(result) > 0:
                    result += "-" + group
                else:
                    result += group

            idx += 1

        return result[::-1]
