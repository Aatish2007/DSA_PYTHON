


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float("inf")

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                window_length = right - left + 1
                min_length = min(min_length, window_length)

                current_sum -= nums[left]
                left += 1

        return 0 if min_length == float("inf") else min_length
'''
#BRUTEFORCE APPROACH
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n=len(nums)
        min_length=float("inf")
        for low in range(n):
            curr_sum=0
            for high in range(low,n):
                curr_sum+=nums[high]
                if curr_sum>=target:
                    min_length=min(min_length,high-low+1)
                    break
        return 0 if min_length==float("inf") else min_length
'''