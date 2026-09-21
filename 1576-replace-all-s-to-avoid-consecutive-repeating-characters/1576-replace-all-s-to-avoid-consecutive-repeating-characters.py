class Solution:
    def modifyString(self, s: str) -> str:
        n = len(s)
        result = ""
        options = ["a", "b", "c"]

        for idx, st in enumerate(s):
            if st != "?":
                result += st
            else:
                if idx == 0:
                    if n == 1:
                        result += options[0]
                    else:
                        for opt in options:
                            if s[idx + 1] != opt:
                                result += opt
                                break

                elif idx == n - 1:
                    for opt in options:
                        if result[-1] != opt:
                            result += opt
                            break
                else:
                    for opt in options:
                        if result[-1] != opt and s[idx + 1] != opt:
                            result += opt
                            break
        
        return result
