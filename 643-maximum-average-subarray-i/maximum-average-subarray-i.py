"""brute force
class Solution:
    def findMaxAverage (self,nums,k):
        max_avg=float("-inf")
        for i in range(len(nums)-k+1):
            total=0
            for j in range(i,i+k):
                total+=nums[j]
                avg=total/k
                if avg>max_avg:
                    max_avg=avg
        return max_avg

"""
#sliding window
class Solution:
    def findMaxAverage(self,nums,k):
        window_sum=sum(nums[:k])
        max_sum=window_sum
        for i in range(k,len(nums)):
            window_sum=window_sum-nums[i-k]+nums[i]
            max_sum=max(max_sum,window_sum)
        return max_sum/k
   