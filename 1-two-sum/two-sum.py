'''
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_map:
                return [num_map[diff], i]
            num_map[num] = i
        return []
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums=sorted((num,i)for i,num in enumerate(nums))
        i=0
        j=len(sorted_nums)-1
        while(i<j):
            curr_sum=sorted_nums [i][0]+sorted_nums[j][0]
            if curr_sum==target:
                return[sorted_nums[i][1],sorted_nums[j][1]]
            elif curr_sum<target:
                i+=1
            else:
                j-=1
        return[]   