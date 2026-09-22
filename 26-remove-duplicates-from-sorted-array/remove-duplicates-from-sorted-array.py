#BRUTEFORCE APPORACH
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        temp=[]
        for num in nums:
            if not temp or temp[-1]!=num:
                temp.append(num)
        for i in range (len(temp)):
            nums[i]=temp[i]
        return len(temp)
        