class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        opened = 0
        
        for c in s:
            if c == '(':
                # If it's an opening brace and we are already inside a primitive string, 
                # keep it. Only the outermost '(' has opened == 0.
                if opened > 0:
                    ans.append(c)
                opened += 1
            else:  # c == ')'
                opened -= 1
                # If after decrementing we are still inside a primitive string,
                # keep it. Only the outermost ')' will bring opened down to 0.
                if opened > 0:
                    ans.append(c)
                    
        return "".join(ans)
