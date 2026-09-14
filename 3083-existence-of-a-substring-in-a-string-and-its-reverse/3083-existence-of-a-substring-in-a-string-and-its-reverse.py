class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        store = set()
        n = len(s)

        for i in range(n-2, -1, -1):
            store.add(s[i+1] + s[i])
        
        for i in range(1, n):
            cand = s[i-1] + s[i]
            if cand in store:
                return True

        return False