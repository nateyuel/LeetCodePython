class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings) // 2
        store = defaultdict(set)

        for idx in range(n):
            store[rings[idx * 2 + 1]].add(rings[idx * 2])
        
        result = 0
        for rods, rings in store.items():
            if len(rings) == 3:
                result += 1
        
        return result