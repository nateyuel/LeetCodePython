class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        long_ones = 0
        long_zeros = 0

        curr_ones = 0
        curr_zeros = 0
        for ch in s:
            if ch == "1":
                long_zeros = max(long_zeros, curr_zeros)
                curr_zeros = 0
                curr_ones += 1
            else:
                long_ones = max(long_ones, curr_ones)
                curr_ones = 0
                curr_zeros += 1
        
        long_zeros = max(long_zeros, curr_zeros)
        long_ones = max(long_ones, curr_ones)

        return long_ones > long_zeros
                