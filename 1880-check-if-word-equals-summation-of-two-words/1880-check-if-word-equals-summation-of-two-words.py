class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        conc1 = ""
        conc2 = ""
        conc3 = ""

        for ch in firstWord:
            conc1 += str(ord(ch) - 97)
        for ch in secondWord:
            conc2 += str(ord(ch) - 97)
        for ch in targetWord:
            conc3 += str(ord(ch) - 97)

        return int(conc3) == (int(conc1) + int(conc2))