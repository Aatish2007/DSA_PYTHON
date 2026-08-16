from collections import Counter
class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        count = Counter(stone % 3 for stone in stones)

        cnt0 = count[0]
        cnt1 = count[1]
        cnt2 = count[2]
        if cnt0 % 2 == 0:
            return min(cnt1, cnt2) > 0
        else:
            return abs(cnt1 - cnt2) > 2