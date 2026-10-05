class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        store = defaultdict(list)
        parents = []

        for idx, ch in enumerate(s):
            if ch == "(":
                if parents:
                    store[idx] = [parents[-1], [], []]
                    store[parents[-1]][1].append(idx)
                else:
                    store[idx] = [idx, [], []]

                parents.append(idx)

            else:
                parents.pop()
        
        def dfs(idx):
            if not store[idx][1]:
                if store[idx][2]:
                    return 2 * sum(store[idx][2])
                else:
                    return 1

            while store[idx][1]:
                poped = store[idx][1].pop()
                visited.add(poped)
                store[idx][2].append(dfs(poped))

            return 2 * sum(store[idx][2]) if store[idx][2] else 1
        
        visited = set()
        result = 0

        for idx, (parent, childrens, scores) in store.items():
            if idx not in visited:
                result += dfs(idx)
 
        return result 



