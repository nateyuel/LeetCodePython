class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        result = 0

        for word in words:
            valid = True
            for ch in brokenLetters:
                if word.count(ch) > 0:
                    valid = False
                    break

            if valid:
                result += 1

        return result
