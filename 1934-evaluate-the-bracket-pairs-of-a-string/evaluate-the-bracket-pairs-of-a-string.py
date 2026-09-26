from typing import List

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # Step 1: Convert the knowledge list into a hash map for O(1) lookups
        d = {key: value for key, value in knowledge}
        
        res = []
        is_inside_bracket = False
        current_key = []
        
        # Step 2: Iterate through the string character by character
        for char in s:
            if char == '(':
                is_inside_bracket = True
            elif char == ')':
                is_inside_bracket = False
                # Form the key and look it up in the dictionary
                key_str = "".join(current_key)
                res.append(d.get(key_str, '?'))
                current_key = []  # Reset for the next bracket pair
            else:
                if is_inside_bracket:
                    current_key.append(char)
                else:
                    res.append(char)
                    
        return "".join(res)
