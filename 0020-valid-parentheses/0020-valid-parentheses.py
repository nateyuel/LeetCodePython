class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in ("(", "{", "["):
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False

                if ch == ")":
                    if stack[-1] != "(":
                        return False
                    else:
                        stack.pop()
                elif ch == "}":
                    if stack[-1] != "{":
                        return False
                    else:
                        stack.pop()
                else:
                    if stack[-1] != "[":
                        return False
                    else:
                        stack.pop()

        return not stack