from functools import cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        @cache
        def dfs(i: int, m: int) -> int:
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            max_stones = 0
            for x in range(1, 2 * m + 1):
                opponent_score = dfs(i + x, max(m, x))
                current_score = suffix_sum[i] - opponent_score
                max_stones = max(max_stones, current_score)
                
            return max_stones

        return dfs(0, 1)