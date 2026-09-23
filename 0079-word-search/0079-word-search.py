class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        l = len(word)

        if l == 0:
            return True
        if m == 0 or n == 0:
            return False
        if m * n < l:
            return False

        def dfs(row, col, idx):
            if idx == l:
                return True

            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[idx]:
                return False

            org = board[row][col]
            board[row][col] = "#"

            for (dr, dc) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if dfs(row + dr, col + dc, idx + 1):
                    return True
                    
            board[row][col] = org
            return False

        for row in range(m):
            for col in range(n):
                if dfs(row, col, 0):
                    return True
    
        return False