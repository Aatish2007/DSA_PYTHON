class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize a pointer to track the position for valid elements
        valid_index = 0
      
        # Iterate through each element in the array
        for current_num in nums:
            # If current element is not the value to be removed
            if current_num != val:
                # Place it at the valid_index position
                nums[valid_index] = current_num
                # Move the valid_index pointer forward
                valid_index += 1
      
        # Return the count of elements that are not equal to val
        return valid_index
