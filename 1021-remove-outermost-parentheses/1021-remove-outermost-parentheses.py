class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        remove_idexes = set()
        stack = []
        result = ""

        for idx, ch in enumerate(s):
            if ch == "(":
                if not stack:
                    remove_idexes.add(idx)
                stack.append(idx)
            else:
                if len(stack) == 1:
                    remove_idexes.add(idx)
                stack.pop()

            if idx not in remove_idexes:
                result += ch
        
        return result
