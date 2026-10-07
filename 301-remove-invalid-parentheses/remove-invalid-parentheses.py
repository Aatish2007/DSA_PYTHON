class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Helper function to check if a string has valid parentheses
        def isValid(string: str) -> bool:
            balance = 0
            for char in string:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                    # If balance drops below 0, there are unmatched closing brackets
                    if balance < 0:
                        return False
            return balance == 0

        # Queue for BFS, initialized with the original string
        level = {s}
        
        while level:
            # Filter the current level for any valid strings
            valid_strings = list(filter(isValid, level))
            
            # If valid strings are found at this level, they have the minimum removals
            if valid_strings:
                return valid_strings
            
            # Generate the next level by removing one bracket from each string in the current level
            next_level = set()
            for current_str in level:
                for i in range(len(current_str)):
                    # Only try removing parentheses, skip letters
                    if current_str[i] in ('(', ')'):
                        new_str = current_str[:i] + current_str[i+1:]
                        next_level.add(new_str)
            
            level = next_level
            
        return [""]
