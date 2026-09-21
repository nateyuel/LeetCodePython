class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        if current == correct:
            return 0
        
        rem_min = (int(correct[:2]) * 60 + int(correct[3:])) - (int(current[:2]) * 60 + int(current[3:]))

        min_opr = 0
        for opr_min in (60, 15, 5, 1):
            min_opr += rem_min // opr_min
            rem_min %= opr_min
        
        return min_opr