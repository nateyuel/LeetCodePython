class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        drs = (-1, 0, 1, 0, -1)

        def dfs(i, j):
            total = grid[i][j]
            grid[i][j] = 0

            for d in range(4):
                x, y = i + drs[d], j + drs[d + 1]
                if 0 <= x < m and 0 <= y < n and grid[x][y] > 0:
                    total += dfs(x, y)

            return total
        
        return sum(
            grid[i][j] and dfs(i, j) % k == 0 
            for i in range(m)
            for j in range(n)
        )