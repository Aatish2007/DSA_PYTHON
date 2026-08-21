from math import gcd
from typing import List


class Solution:

    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        # Precompute LCM and sign (-1^|S|+1) for all 2^n - 1 non-empty subsets
        subsets = []
        for mask in range(1, 1 << n):
            lcm_val = 1
            bits_count = 0

            for i in range(n):
                if (mask >> i) & 1:
                    bits_count += 1
                    lcm_val = (lcm_val * coins[i]) // gcd(lcm_val, coins[i])

            sign = 1 if bits_count % 2 == 1 else -1
            subsets.append((lcm_val, sign))

        # Function to count numbers <= M divisible by at least one coin
        def count_valid(M: int) -> int:
            total = 0
            for lcm_val, sign in subsets:
                total += sign * (M // lcm_val)
            return total

        # Binary Search on the answer space
        low = 1
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count_valid(mid) >= k:
                ans = mid
                high = mid - 1  # Try to find a smaller valid amount
            else:
                low = mid + 1  # Amount too small, search right

        return ans