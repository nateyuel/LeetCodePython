class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(curr_str, open_count, close_count):
            if len(curr_str) == n * 2:
                result.append(curr_str)
            
            if open_count < n:
                backtrack(curr_str + "(", open_count + 1, close_count)
            
            if close_count < open_count:
                backtrack(curr_str + ")", open_count, close_count + 1)
            
            return result

        return backtrack("", 0, 0)        