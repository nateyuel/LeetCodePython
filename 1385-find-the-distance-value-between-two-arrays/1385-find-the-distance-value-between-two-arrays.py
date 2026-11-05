class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        result = 0

        for num in arr1:
            valid = True
            for num2 in arr2:
                if not valid:
                    break
                if abs(num - num2) <= d:
                    valid = False
            
            if valid:
                result += 1
            
        return result 