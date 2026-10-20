class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        diff = []
        n = len(s)

        if n != len(goal):
            return False

        for idx in range(n):
            if s[idx] != goal[idx]:
                diff.append(idx)
        
        if len(diff) > 2 or len(diff) == 1:
            return False
        
        if len(diff) == 2:
            if s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]:
                return True
            else:
                return False
        
        if len(set(s)) < len(s):
            return True
        
        return False