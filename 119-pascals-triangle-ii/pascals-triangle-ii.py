class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        for j in range(1, rowIndex + 1):
            next_val = row[-1] * (rowIndex - j + 1) // j
            row.append(next_val)
        return row