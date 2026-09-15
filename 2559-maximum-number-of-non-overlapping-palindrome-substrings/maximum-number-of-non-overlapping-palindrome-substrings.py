class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        
        # Helper to check if s[i..j] is a palindrome
        is_pal = [[False] * n for _ in range(n)]
        
        # Every single character is a palindrome of length 1
        for i in range(n):
            is_pal[i][i] = True
            
        # Check for even length palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                is_pal[i][i + 1] = True
                
        # Check for lengths 3 to n
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and is_pal[i + 1][j - 1]:
                    is_pal[i][j] = True
                    
        # DP to find max non-overlapping palindromes of length >= k
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            # Try palindrome ending at i-1 with length k or k+1
            for length in (k, k + 1):
                start = i - length
                if start >= 0 and is_pal[start][i - 1]:
                    dp[i] = max(dp[i], dp[start] + 1)
                    
        return dp[n]
