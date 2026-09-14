class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        tracker = defaultdict(list)

        for idx, ch in enumerate(s):
            if ch not in tracker:
                tracker[ch] = [idx, -1]
            else:
                tracker[ch][1] = idx
        
        result = -1

        for (left, right) in tracker.values():
            if right != -1:
                result = max(result, right - left - 1)
        
        return result