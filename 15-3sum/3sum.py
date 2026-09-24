'''
#BRUTE FORCE APPORACH
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        triplet=tuple(sorted([nums[i],nums[j],nums[k]]))
                        result.add(triplet)
        return[list(triplet)for triplet in result]

#BETTER APPORACH USING HASHMAP 
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result=set()
        n=len(nums)
        for i in range(n):
            seen=set()
            for  j in range(i+1,n):
                target= -(nums[i]+nums[j])
                if target in seen :
                    triplet=tuple(sorted([nums[i],nums[j],target]))
                    result.add(triplet)
                seen.add(nums[j])
        return[list(triplet) for triplet in result]   
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort karo
        result = []
        n = len(nums)
        
        for i in range(n - 2):  # Step 2: Har element fix karo
            # Duplicate fix elements skip karo
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Optimization: Agar current element > 0, toh aage koi triplet nahi milega
            if nums[i] > 0:
                break
            
            # Step 3: Two Pointers
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Duplicates skip karo
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                    
                elif current_sum < 0:
                    left += 1  # Sum badhana hai
                else:
                    right -= 1  # Sum ghatana hai
        
        return result
