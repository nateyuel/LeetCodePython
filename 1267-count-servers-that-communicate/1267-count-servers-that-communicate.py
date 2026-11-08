class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        result = set()
        m = len(grid)
        n = len(grid[0])

        for row in range(m):
            cand = set()
            for col in range(n):
                if grid[row][col] == 1:
                    cand.add((row, col))

            if len(cand) > 1:
                result.update(cand)

        for col in range(n):
            cand = set()
            for row in range(m):
                if grid[row][col] == 1:
                    cand.add((row, col))

            if len(cand) > 1:
                result.update(cand)

        return len(result)
