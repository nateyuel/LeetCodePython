import re
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n = len(s)

        letters = re.sub(r"[^a-zA-Z]", "", s)
        letters = letters[::-1]
        non_letters = []
        store = defaultdict()
        count = 0
        result = ""

        for idx, ch in enumerate(s):
            if not ch.isalpha():
                store[len(non_letters)] = count
                non_letters.append(ch)
            else:
                count += 1

        idx = 0
        for idx2, count in store.items():
            while idx < count:
                result += letters[idx]
                idx += 1
            
            result += non_letters[idx2]
        
        result += letters[idx:]

        return result             
        