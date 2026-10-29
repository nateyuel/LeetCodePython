class Solution:
    def reformatNumber(self, number: str) -> str:
        clean_number = number.translate(str.maketrans("", "", " -"))
        result = ""
        n = len(clean_number)
        idx = 0
        
        while idx < n:
            if (n - idx) % 3 == 0 or n - idx >= 5:
                if result:
                    result += "-"

                result += clean_number[idx:idx + 3]
                idx += 3
            else:
                if result:
                    result += "-"

                result += clean_number[idx:idx + 2]
                idx += 2
        
        return result 