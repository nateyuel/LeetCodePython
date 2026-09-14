class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        if n <= k:
            return s[::-1]
        
        idx = k - 1
        result = s[:k][::-1]
        turn = 0

        while idx < n:
            if turn == 0:
                if idx + k < n:
                    result += s[idx+1:idx+k+1]
                    turn = 1
                    idx += k
                elif idx + 1 < n:
                    result += s[idx+1:]
                    break
                else:
                    break
            else:
                if idx + k < n:
                    result += s[idx+1:idx+k+1][::-1]
                    turn = 0
                    idx += k
                elif idx + 1 < n:
                    result += s[idx+1:][::-1]
                    break
                else:
                    break
            
        return result