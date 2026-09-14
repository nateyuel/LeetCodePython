class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = len(name)
        m = len(typed)
        i = 0 
        j = 0

        while i < n and j < m:
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif i > 0 and name[i-1] == typed[j]:
                j += 1
            else:
                return False
        
        while j < m:
            if typed[j] != name[-1]:
                return False
            else:
                j += 1
        
        while i < n:
            if name[i] != typed[-1]:
                return False
            else:
                i += 1

        return True