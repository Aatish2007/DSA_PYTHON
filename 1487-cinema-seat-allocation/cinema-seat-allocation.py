from collections import defaultdict
from typing import List


class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_map = defaultdict(set)
        for row, seat in reservedSeats:
            if seat in {2, 3, 4, 5, 6, 7, 8, 9}:
                reserved_map[row].add(seat)
        ans = (n - len(reserved_map)) * 2
        for row, seats in reserved_map.items():
            left_free = not (seats & {2, 3, 4, 5})
            right_free = not (seats & {6, 7, 8, 9})
            middle_free = not (seats & {4, 5, 6, 7})

            if left_free and right_free:
                ans += 2
            elif left_free or right_free or middle_free:
                ans += 1

        return ans