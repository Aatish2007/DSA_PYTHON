'''bruteforce
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            for j in range(i,n):
                subarray=nums[i:j+1]
                distinct=len(set(subarray))
                ans+=distinct*distinct
        return ans
'''
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            seen=set()
            for j in range(i,n):
                seen.add(nums[j])
                distinct=len(seen)
                ans+=distinct*distinct
        return ans
