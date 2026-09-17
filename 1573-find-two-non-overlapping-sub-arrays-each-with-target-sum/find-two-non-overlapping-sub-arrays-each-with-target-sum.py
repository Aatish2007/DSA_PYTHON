from typing import List


class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float("inf")
        min_len = [INF] * n

        ans = INF
        left = 0
        window_sum = 0
        best_till_now = INF

        for right in range(n):
            window_sum += arr[right]
            while window_sum > target:
                window_sum -= arr[left]
                left += 1
            if window_sum == target:
                curr_len = right - left + 1
                if left > 0 and min_len[left - 1] != INF:
                    ans = min(ans, curr_len + min_len[left - 1])

                best_till_now = min(best_till_now, curr_len)
            min_len[right] = best_till_now

        return ans if ans != INF else -1