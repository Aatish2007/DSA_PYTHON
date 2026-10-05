class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                v = stack.pop()
                # If v is 0, it means "()", score is 1. 
                # Otherwise it's nested "(A)", score is 2 * v.
                score = max(2 * v, 1)
                stack[-1] += score
                
        return stack[0]
