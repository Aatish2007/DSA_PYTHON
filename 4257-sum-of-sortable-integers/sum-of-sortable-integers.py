import math

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Precompute adjacent descents (drops) count prefix sum
        drops = [0] * n
        for i in range(1, n):
            drops[i] = drops[i - 1] + (1 if nums[i - 1] > nums[i] else 0)
            
        def can_rotate_sorted(start: int, length: int) -> bool:
            """Checks if subarray nums[start : start + length] can be cyclically rotated to sorted order."""
            if length == 1:
                return True
            
            end = start + length - 1
            # Number of drops inside the block range [start, end]
            internal_drops = drops[end] - drops[start]
            
            # Wrap-around drop from last element back to first element of the block
            wrap_drop = 1 if nums[end] > nums[start] else 0
            
            # A circular array can be sorted by rotation iff total circular drops <= 1
            return (internal_drops + wrap_drop) <= 1

        def is_sortable(k: int) -> bool:
            """Validates whether divisor k can partition and sort the array."""
            prev_max = float('-inf')
            
            for start in range(0, n, k):
                # 1. Check if the block itself can be rotated to sorted order
                if not can_rotate_sorted(start, k):
                    return False
                
                # 2. Check if block minimum is >= previous block's maximum
                block_min = min(nums[start : start + k])
                block_max = max(nums[start : start + k])
                
                if block_min < prev_max:
                    return False
                
                prev_max = block_max
                
            return True

        # Find all divisors of n and sum up sortable block sizes
        ans = 0
        for k in range(1, int(math.isqrt(n)) + 1):
            if n % k == 0:
                if is_sortable(k):
                    ans += k
                
                # Check the paired divisor n // k if it's different from k
                other_k = n // k
                if other_k != k and is_sortable(other_k):
                    ans += other_k
                    
        return ans