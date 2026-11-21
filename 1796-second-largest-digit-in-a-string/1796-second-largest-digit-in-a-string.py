class Solution:
    def secondHighest(self, s: str) -> int:
        set_s = set(s)
        only_digits = sorted(
            list(int(char) for char in set_s if char.isdigit()), reverse=True
        )

        if len(only_digits) > 1:
            return only_digits[1]
        else:
            return -1
