from collections import Counter
from typing import List


class Solution:

    def totalNumbers(self, digits: List[int]) -> int:
        freq = Counter(digits)
        valid_count = 0

        # Iterate through all 3-digit even numbers (100 to 998, step by 2)
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10

            req = Counter([d1, d2, d3])

            # Check if current number can be formed using available digits
            if all(freq[digit] >= count for digit, count in req.items()):
                valid_count += 1

        return valid_count