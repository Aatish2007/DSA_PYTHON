
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        
        '''#BRUTEFORCE
        for i in range(n):
            nums1[m+i]=nums2[i]
        nums1.sort()
        
        #BETTER APPORACH
        temp=[]
        i=j=0
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                temp.append(nums1[i])
                i+=1
            else:
                temp.append(nums2[j])
        while i<m:
            temp.append(nums1[i])
            i+=1
        while j<n:
            temp.append(nums2[j])
            j+=1
        for k in range(len(temp)):
            nums1[k]=temp[k]
        '''
        i=m-1
        j=n-1
        k=m+n-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                  nums1[k]=nums1[i]
                  i-=1
            else:
                 nums1[k]=nums2[j]
                 j-=1
            k-=1
        while j>=0:
             nums1[k]=nums2[j]
             j-=1
             k-=1