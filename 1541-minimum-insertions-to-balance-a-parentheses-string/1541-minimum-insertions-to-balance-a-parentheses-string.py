class Solution:
    def minInsertions(self, s: str) -> int:
        s += "("
        stack = []
        result = 0
        cons_close = 0

        for idx, ch in enumerate(s):
            if ch == "(":
                if cons_close > 0:
                    n = len(stack)
                    rem = cons_close % 2
                    div = cons_close // 2

                    if n < div:
                        result += div - n
                        if rem:
                            result += 2
                        stack = []
                    else:
                        while div > 0:
                            stack.pop()
                            div -= 1

                        if rem:
                            if len(stack) > 0:
                                result += 1
                                stack.pop()
                            else:
                                result += 2
                        
                    cons_close = 0

                if idx < len(s) - 1:
                    stack.append("(")

            else:
                cons_close += 1

        result += len(stack) * 2

        return result
