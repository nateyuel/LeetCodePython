class Solution:
    def getSmallestString(self, s: str) -> str:
        n = len(s)
        store = list(s)

        for idx in range(1, n):
            if int(s[idx - 1]) > int(s[idx]) and int(s[idx - 1]) % 2 == int(s[idx]) % 2:
                store[idx - 1], store[idx] = store[idx], store[idx - 1]
                return "".join(store)

        return s
