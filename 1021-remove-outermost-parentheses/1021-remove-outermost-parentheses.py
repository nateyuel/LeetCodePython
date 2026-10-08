class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        result = ""

        for idx, ch in enumerate(s):
            if ch == "(":
                if stack:
                    result += ch
                stack.append(idx)
            else:
                if len(stack) > 1:
                    result += ch

                stack.pop()
        
        return result
