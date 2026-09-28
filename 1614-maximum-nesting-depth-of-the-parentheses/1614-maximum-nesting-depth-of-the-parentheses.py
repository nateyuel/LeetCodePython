class Solution:
    def maxDepth(self, s: str) -> int:
        max_nested = 0
        stack = []

        for ch in s:
            if ch == "(":
                stack.append("(")
            elif ch == ")":
                max_nested = max(max_nested, len(stack))
                stack.pop()
        
        return max_nested