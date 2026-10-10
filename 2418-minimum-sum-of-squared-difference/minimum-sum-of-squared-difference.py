class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # Calculate absolute differences
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        
        # Total operations available
        k = k1 + k2
        
        # If total operations can reduce all differences to 0
        if sum(diffs) <= k:
            return 0
        
        # Sort differences in descending order and add a dummy 0 at the end
        diffs.sort(reverse=True)
        diffs.append(0)
        
        n = len(diffs) - 1
        for i in range(n):
            # Number of elements currently at the maximum value
            count = i + 1
            # Drop to the next unique value
            gap = diffs[i] - diffs[i + 1]
            
            # Total operations required to bring all current max elements down to the next level
            total_needed = count * gap
            
            if k >= total_needed:
                k -= total_needed
            else:
                # We cannot bring all elements down to diffs[i+1]
                # Distribute the remaining k operations evenly
                q, r = divmod(k, count)
                
                # The base value for the elements up to index i
                base_val = diffs[i] - q
                
                # r elements will be reduced by one more than the others
                ans = 0
                ans += r * (base_val - 1) ** 2
                ans += (count - r) * base_val ** 2
                
                # Add the square of the remaining un-mutated elements
                for j in range(i + 1, n):
                    ans += diffs[j] ** 2
                    
                return ans
                
        return 0
