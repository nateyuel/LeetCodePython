class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        pos = {0: -1}
        n = len(arr)
        s = 0
        res = n+1 
        min_len = n

        for idx, num in enumerate(arr):
            s += num
            if s - target in pos:
                j = pos[s-target]
                length = idx-j
                res = min(res, length+(n if j==-1 else arr[j]))
                min_len = min(min_len, length)
            
            arr[idx] = min_len
            pos[s] = idx
        
        return -1 if res == n+1 else res