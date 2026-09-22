'''BRUTEFORCE APPORACH
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        temp=[]
        for num in nums:
            if not temp or temp[-1]!=num:
                temp.append(num)
        for i in range (len(temp)):
            nums[i]=temp[i]
        return len(temp)

#BETTER APPORACH USING SET()
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        set_1=set()
        for num in nums:
            set_1.add(num)
        sorted_set=sorted(set_1)
        for i in range(len(sorted_set)):
            nums[i]=sorted_set[i]
        return len(sorted_set)
'''
#OPTIMAL APPORACH 
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        i=0
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
        return i+1