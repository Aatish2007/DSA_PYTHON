class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(open_count, close_count, current_str):
            # Base case: valid string of length 2n found
            if open_count == n and close_count == n:
                res.append(current_str)
                return
            
            # Rule 1: We can always add an open parenthesis if we have remaining pairs
            if open_count < n:
                backtrack(open_count + 1, close_count, current_str + "(")
                
            # Rule 2: We can only add a close parenthesis if it doesn't exceed open ones
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_str + ")")
                
        backtrack(0, 0, "")
        return res
