class Solution:
    def checkValidString(self, s: str) -> bool:
        # Track the minimum and maximum possible open parentheses counts
        min_open = 0
        max_open = 0
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            else:  # char == '*'
                # If '*' is ')', it decreases min_open
                min_open -= 1
                # If '*' is '(', it increases max_open
                max_open += 1
            
            # If max_open is negative, there are too many ')' brackets 
            # and no combination of choices can make the string valid.
            if max_open < 0:
                return False
                
            # min_open cannot drop below 0 because we can choose to treat 
            # excessive '*' as empty strings instead of closing brackets.
            if min_open < 0:
                min_open = 0
                
        # The string is valid if we can exactly balance all parentheses
        return min_open == 0
