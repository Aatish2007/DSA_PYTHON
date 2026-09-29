from functools import lru_cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Quick checks:
        # 1. Total path length (m + n - 1) must be even for valid parentheses.
        # 2. Path must start with '(' and end with ')'.
        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        
        max_possible_balance = (m + n - 1) // 2

        @lru_cache(None)
        def dfs(r: int, c: int, balance: int) -> bool:
            # Update balance for current cell
            if grid[r][c] == '(':
                balance += 1
            else:
                balance -= 1
            
            # Invalid path conditions:
            # - balance drops below 0
            # - balance exceeds maximum needed balance
            if balance < 0 or balance > max_possible_balance:
                return False
            
            # Reached destination cell
            if r == m - 1 and c == n - 1:
                return balance == 0
            
            # Move Down or Right
            down = dfs(r + 1, c, balance) if r + 1 < m else False
            right = dfs(r, c + 1, balance) if c + 1 < n else False
            
            return down or right

        return dfs(0, 0, 0)