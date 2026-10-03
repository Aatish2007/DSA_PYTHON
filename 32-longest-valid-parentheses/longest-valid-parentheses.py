class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize with a sentinel value
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # Push the index of the open parenthesis
                stack.append(i)
            else:
                # Pop the last element (either a matching '(' or a sentinel)
                stack.pop()
                
                if not stack:
                    # If empty, the current index becomes the new baseline sentinel
                    stack.append(i)
                else:
                    # Calculate the length of the current valid substring
                    max_length = max(max_length, i - stack[-1])
                    
        return max_length

