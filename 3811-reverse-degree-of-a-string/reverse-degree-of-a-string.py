class Solution:
    def reverseDegree(self, s: str) -> int:
        total_score = 0
        for i, c in enumerate(s):
            reverse_alpha_val = 26 - (ord(c) - ord('a'))
            total_score += reverse_alpha_val * (i + 1)
        return total_score
