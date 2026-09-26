class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        result = ""
        pairs = {knowledge[idx][0]:knowledge[idx][1] for idx in range(len(knowledge))}
        key = ""
        brace_open = False

        for ch in s:
            if ch == "(":
                brace_open = True
                continue
            elif ch == ")":
                value = pairs.get(key)
                if not value:
                    result += "?"
                else:
                    result += value
                brace_open = False
                key = ""
                continue 

            if brace_open:
                key += ch
            else:
                result += ch
            
        return result