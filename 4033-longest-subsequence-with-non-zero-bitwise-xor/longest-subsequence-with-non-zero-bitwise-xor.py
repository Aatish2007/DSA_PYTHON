import functools

class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        # Case 1: If all elements are zero, no non-zero XOR subsequence can be formed
        if all(x == 0 for x in nums):
            return 0
        
        # Calculate the bitwise XOR sum of all elements
        total_xor = functools.reduce(lambda x, y: x ^ y, nums, 0)
        
        # Case 2: The entire array's XOR is already non-zero
        if total_xor != 0:
            return len(nums)
        
        # Case 3: Total XOR is zero, but elements are not all zero. 
        # Removing any single non-zero element will break the zero-sum balance.
        return len(nums) - 1
