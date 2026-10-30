class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        a, b = s.split(':')
        
        return [chr(c) + str(r)
                for c in range(ord(a[0]), ord(b[0]) + 1)
                for r in range(int(a[1:]), int(b[1:]) + 1)]