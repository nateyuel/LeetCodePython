class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        a_subs = set()
        b_subs = set()
        a_len = len(a)
        b_len = len(b)
        result = -1

        for i in range(a_len):
            for j in range(i + 1, a_len + 1):
                a_subs.add(a[i:j])

        for i in range(b_len):
            for j in range(i + 1, b_len + 1):
                cand = b[i:j]
                b_subs.add(cand)
                if cand not in a_subs:
                    result = max(result, len(cand))
        
        for i in range(a_len):
            for j in range(i + 1, a_len + 1):
                cand = a[i:j]
                if cand not in b_subs:
                    result = max(result, len(cand))
        
        return result 

