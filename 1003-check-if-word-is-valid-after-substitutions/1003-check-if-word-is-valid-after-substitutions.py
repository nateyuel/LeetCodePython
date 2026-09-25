class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            stack.append(ch)

            if len(stack) >= 3 and "".join(stack[-3:]) == "abc":
                del stack[-3:]

        return not stack