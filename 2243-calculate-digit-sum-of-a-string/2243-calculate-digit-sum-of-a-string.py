class Solution:
    def digitSum(self, s: str, k: int) -> str:
        result  = s 

        while len(result) > k :
            next_result = ""
            curr = -99
            for i in range(len(result)) :
                if curr == -99 :
                    curr = int(result[i])
                else:
                    curr += int(result[i])
                if (i+1)%k == 0 :
                    next_result += str(curr)
                    curr = -99
            if curr != -99 :
                next_result += str(curr)
             
            result = next_result

        return result
                

        