class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        result = []
        freq = 0
        last_idx = 0

        for num in nums:
            if num == target:
                freq += 1
            elif num < target:
                last_idx += 1
        
        while freq > 0:
            result.append(last_idx)
            last_idx += 1
            freq -= 1
        
        return result 

