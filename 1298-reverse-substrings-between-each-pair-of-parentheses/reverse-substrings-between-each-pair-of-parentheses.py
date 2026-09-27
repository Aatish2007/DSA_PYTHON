class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                # Collect characters until the matching '('
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                # Pop the '(' itself
                if stack and stack[-1] == '(':
                    stack.pop()
                # Push the reversed characters back to the stack
                stack.extend(temp)
            else:
                stack.append(char)
        
        return "".join(stack)
