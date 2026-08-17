class Solution:

    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        if n == 1:
            return 0

        # 1. Prefix sum array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # dp[i][j] stores the max score for stoneValue[i...j]
        dp = [[0] * n for _ in range(n)]

        # max_left[i][j] = max_{i <= k <= j} (S(i, k) + dp[i][k])
        max_left = [[0] * n for _ in range(n)]

        # max_right[i][j] = max_{i <= k <= j} (S(k, j) + dp[k][j])
        max_right = [[0] * n for _ in range(n)]

        # Base case initialization for length 1
        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]

        # 2. DP over range length
        for length in range(2, n + 1):
            mid_k = 0  # Two pointer candidate for partition

            for i in range(n - length + 1):
                j = i + length - 1

                # Adjust mid_k so prefix[mid_k + 1] - prefix[i] <= total_sum / 2
                if mid_k < i:
                    mid_k = i

                total_sum = prefix[j + 1] - prefix[i]

                while (
                    mid_k < j
                    and (prefix[mid_k + 1] - prefix[i]) * 2 <= total_sum
                ):
                    mid_k += 1

                mid_k -= 1  # Largest k where left_sum <= right_sum

                res = 0

                # Case 1: Left sum < Right sum (valid k range: i to mid_k - 1)
                # If left_sum == right_sum at mid_k, handle it separately
                left_sum_mid = prefix[mid_k + 1] - prefix[i]
                right_sum_mid = prefix[j + 1] - prefix[mid_k + 1]

                if left_sum_mid == right_sum_mid:
                    # Equal sums at mid_k
                    res = max(
                        res,
                        left_sum_mid
                        + max(dp[i][mid_k], dp[mid_k + 1][j]),
                    )
                    k_left_end = mid_k - 1
                else:
                    k_left_end = mid_k

                # Best score when left_sum < right_sum using precomputed max_left
                if k_left_end >= i:
                    res = max(res, max_left[i][k_left_end])

                # Best score when right_sum < left_sum using precomputed max_right
                k_right_start = mid_k + 1
                if left_sum_mid == right_sum_mid:
                    k_right_start += 1

                if k_right_start <= j - 1:
                    res = max(res, max_right[k_right_start + 1][j])

                dp[i][j] = res

                # Update max_left and max_right tables for O(1) future lookups
                max_left[i][j] = max(max_left[i][j - 1], total_sum + dp[i][j])
                max_right[i][j] = max(
                    max_right[i + 1][j], total_sum + dp[i][j]
                )

        return dp[0][n - 1]