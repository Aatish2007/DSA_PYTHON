class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Jab tak "()" pair hai, tab tak remove karo
        while '()' in s:
            s = s.replace('()', '')
        
        # Jo bach gaya, woh sab unmatched hai
        return len(s)