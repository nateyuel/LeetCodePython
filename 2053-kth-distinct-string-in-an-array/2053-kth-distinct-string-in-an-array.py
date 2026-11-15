class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        store = Counter(arr)
        distinct_count = 0

        for cand in arr:
            if store[cand] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return cand

        return ""
