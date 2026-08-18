from collections import Counter
from typing import List


class Solution:

    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = Counter(nums)

        if k == 1:
            ans = -1
            for num, count in freq.items():
                if count == 1:
                    ans = max(ans, num)
            return ans

        if k == n:
            return max(nums)

        candidates = []

        if freq[nums[0]] == 1:
            candidates.append(nums[0])

        if nums[n - 1] != nums[0] and freq[nums[n - 1]] == 1:
            candidates.append(nums[n - 1])

        return max(candidates) if candidates else -1