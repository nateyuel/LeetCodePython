class Solution:
    def checkValidString(self, s: str) -> bool:
        star_stack = []
        stack = []

        for idx, ch in enumerate(s):
            if ch == "*":
                star_stack.append(idx)
            elif ch == "(":
                stack.append(idx)
            elif ch == ")":
                if stack:
                    stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
        if len(stack) > len(star_stack):
            return False

        while stack and star_stack:
            if stack[-1] < star_stack[-1]:
                stack.pop() 
                star_stack.pop()
            else:
                return False

        return True
                    