class Solution:
    def reformat(self, s: str) -> str:
        digits = ""
        letters = ""

        for ch in s:
            if ch.isnumeric():
                digits += ch
            else:
                letters += ch

        if abs(len(digits) - len(letters)) <= 1:
            result = ""
            i = 0
            if len(digits) >= len(letters):

                while i < len(letters):
                    result += digits[i]
                    result += letters[i]
                    i += 1

                if i < len(digits):
                    result += digits[i]

                return result

            else:
                while i < len(digits):
                    result += letters[i]
                    result += digits[i]

                    i += 1

                if i < len(letters):
                    result += letters[i]

            return result

        else:
            return ""
