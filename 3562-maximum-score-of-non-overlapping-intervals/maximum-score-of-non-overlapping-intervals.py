'''
from itertools import combinations
from typing import List


class Solution:

    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        max_weight = -1
        best_indices = []

        # Try selecting k intervals where k ranges from 1 to 4
        for k in range(1, min(5, n + 1)):
            for combo in combinations(range(n), k):
                # Sort chosen intervals by start time to check overlap
                selected = sorted([intervals[i] for i in combo])

                # Check if non-overlapping
                valid = True
                for i in range(len(selected) - 1):
                    if selected[i][1] >= selected[i + 1][0]:
                        valid = False
                        break

                if valid:
                    total_weight = sum(intervals[i][2] for i in combo)
                    sorted_combo = list(sorted(combo))

                    if total_weight > max_weight:
                        max_weight = total_weight
                        best_indices = sorted_combo
                    elif total_weight == max_weight:
                        if not best_indices or sorted_combo < best_indices:
                            best_indices = sorted_combo

        return best_indices
'''
import bisect
from functools import lru_cache
from typing import List


class Solution:

    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Store (left, right, weight, original_index) and sort by start time
        arr = sorted(
            (l, r, w, i) for i, (l, r, w) in enumerate(intervals)
        )
        n = len(arr)

        # Extract start times for binary search
        starts = [x[0] for x in arr]

        @lru_cache(None)
        def dp(i: int, quota: int):
            if i == n or quota == 0:
                return (0, ())

            # Option 1: Skip current interval
            skip_weight, skip_indices = dp(i + 1, quota)

            # Option 2: Pick current interval
            l, r, w, idx = arr[i]
            # Find first interval starting after current interval ends (l > r)
            next_i = bisect.bisect_right(starts, r)

            next_w, next_indices = dp(next_i, quota - 1)
            pick_weight = w + next_w
            pick_indices = tuple(sorted((idx,) + next_indices))

            # Compare Pick vs Skip based on weight, then lexicographical indices
            if pick_weight > skip_weight:
                return (pick_weight, pick_indices)
            elif pick_weight < skip_weight:
                return (skip_weight, skip_indices)
            else:
                return (
                    (pick_weight, pick_indices)
                    if pick_indices < skip_indices
                    else (skip_weight, skip_indices)
                )

        return list(dp(0, 4)[1])