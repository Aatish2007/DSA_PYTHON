class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        max_overlap = 0

        def count_overlap(row_shift: int, col_shift: int) -> int:
            overlap = 0
            for r in range(n):
                for c in range(n):
                    if 0 <= r + row_shift < n and 0 <= c + col_shift < n:
                        if img1[r][c] == 1 and img2[r + row_shift][c + col_shift] == 1:
                            overlap += 1
            return overlap

        for row_shift in range(-n + 1, n):
            for col_shift in range(-n + 1, n):
                max_overlap = max(max_overlap, count_overlap(row_shift, col_shift))

        return max_overlap
