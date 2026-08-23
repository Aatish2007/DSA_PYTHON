class Solution:

    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        sum_left = sum_right = 0
        q_left = q_right = 0

        for i in range(half):
            if num[i] == "?":
                q_left += 1
            else:
                sum_left += int(num[i])

        for i in range(half, n):
            if num[i] == "?":
                q_right += 1
            else:
                sum_right += int(num[i])

        if (q_left + q_right) % 2 == 1:
            return True

        delta_q = q_left - q_right
        delta_s = sum_right - sum_left

        return delta_s != (delta_q // 2) * 9