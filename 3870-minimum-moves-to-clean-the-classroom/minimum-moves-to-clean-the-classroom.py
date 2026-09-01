from collections import deque
from typing import List


class Solution:

    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter_map = {}
        litter_cnt = 0
        start_r = start_c = 0

        for i in range(m):
            for j in range(n):
                cell = classroom[i][j]
                if cell == "S":
                    start_r, start_c = i, j
                elif cell == "L":
                    litter_map[(i, j)] = litter_cnt
                    litter_cnt += 1

        if litter_cnt == 0:
            return 0

        initial_mask = (1 << litter_cnt) - 1

        if (start_r, start_c) in litter_map:
            initial_mask &= ~(1 << litter_map[(start_r, start_c)])

        if initial_mask == 0:
            return 0

        queue = deque([(start_r, start_c, energy, initial_mask)])
        visited = {(start_r, start_c, energy, initial_mask)}

        moves = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            for _ in range(len(queue)):
                r, c, cur_e, mask = queue.popleft()

                if mask == 0:
                    return moves

                if cur_e == 0 and classroom[r][c] != "R":
                    continue

                current_available_energy = (
                    energy if classroom[r][c] == "R" else cur_e
                )

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != "X":
                        target_cell = classroom[nr][nc]

                        nxt_e = (
                            energy
                            if target_cell == "R"
                            else current_available_energy - 1
                        )

                        nxt_mask = mask
                        if (nr, nc) in litter_map:
                            nxt_mask &= ~(1 << litter_map[(nr, nc)])

                        state = (nr, nc, nxt_e, nxt_mask)

                        if state not in visited:
                            visited.add(state)
                            queue.append(state)

            moves += 1

        return -1