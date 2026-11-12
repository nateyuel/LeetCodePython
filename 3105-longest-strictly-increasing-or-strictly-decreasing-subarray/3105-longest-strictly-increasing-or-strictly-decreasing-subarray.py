class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        cont_inc = 1
        cont_dec = 1
        longest = 1

        for idx in range(1, n):
            prev = nums[idx - 1]
            curr = nums[idx]
            if prev > curr:
                cont_dec += 1
                longest = max(longest, cont_inc)
                cont_inc = 1
            elif prev < curr:
                cont_inc += 1
                longest = max(longest, cont_dec)
                cont_dec = 1
            else:
                longest = max(longest, cont_inc, cont_dec)
                cont_inc = 1
                cont_dec = 1

        return max(longest, cont_inc, cont_dec)
