from typing import List


class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float("inf")

        # min_len[i] stores the min length of a valid subarray in arr[0...i]
        min_len = [INF] * n

        ans = INF
        left = 0
        window_sum = 0
        best_till_now = INF

        for right in range(n):
            window_sum += arr[right]

            # Shrink window if sum exceeds target
            while window_sum > target:
                window_sum -= arr[left]
                left += 1

            # Found a valid subarray ending at 'right'
            if window_sum == target:
                curr_len = right - left + 1

                # If there's a valid non-overlapping subarray before 'left'
                if left > 0 and min_len[left - 1] != INF:
                    ans = min(ans, curr_len + min_len[left - 1])

                best_till_now = min(best_till_now, curr_len)

            # Record the best minimum length seen so far up to index 'right'
            min_len[right] = best_till_now

        return ans if ans != INF else -1