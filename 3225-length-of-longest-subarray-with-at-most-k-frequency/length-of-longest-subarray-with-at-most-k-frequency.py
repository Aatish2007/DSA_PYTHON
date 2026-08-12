'''
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans,start=0,-1
        freq=Counter()
        for end in range(len(nums)):
            freq[nums[end]]+=1
            while freq[nums[end]]>k:
                start+=1
                freq[nums[start]]-=1
            ans=max(ans,end-start)
        return ans
'''
#sliding window without nested loops
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        freq=Counter()
        start,char=0,0
        for end in range(n):
            freq[nums[end]]+=1
            if freq[nums[end]]==k+1:
                char+=1
            if char>0:
                freq[nums[start]]-=1
                if freq[nums[start]]==k:
                    char-=1
                start+=1
        return n-start

        