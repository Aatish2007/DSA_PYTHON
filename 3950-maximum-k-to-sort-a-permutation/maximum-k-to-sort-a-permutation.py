class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        res = -1  # -1 in two's complement has all bits set to 1
        
        for i, val in enumerate(nums):
            if i != val:
                res &= val
                
        # If no element was misplaced, res remains -1, so max(res, 0) returns 0
        return max(res, 0)