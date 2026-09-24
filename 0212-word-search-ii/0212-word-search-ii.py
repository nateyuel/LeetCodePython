class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        result = []
        rows = len(board)
        cols = len(board[0])
        word_dict = {word:idx for idx, word in enumerate(words)}


        def dfs(row, col, word):
            if word in word_dict:
                result.append(word)
                del word_dict[word]

            if len(word) >= 10:
                return
            
            temp = board[row][col]
            board[row][col] = "#"

            for dr, dc in ((1,0), (0, 1), (-1, 0), (0, -1)):
                new_row = row + dr
                new_col = col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] != "#":
                    dfs(new_row, new_col, word + board[new_row][new_col])
            
            board[row][col] = temp 
        
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, board[row][col])
            
        return result 
            

        


