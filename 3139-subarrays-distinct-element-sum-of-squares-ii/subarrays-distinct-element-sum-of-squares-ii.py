class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Segment tree nodes store: sum (s), sum of squares (sq), and lazy tag (lazy)
        s = [0] * (4 * n)
        sq = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push(node, l, r):
            if lazy[node] != 0:
                add = lazy[node]
                mid = (l + r) // 2
                
                # Left child update
                left_node = 2 * node
                left_len = mid - l + 1
                sq[left_node] = (sq[left_node] + 2 * add * s[left_node] + add * add * left_len) % MOD
                s[left_node] = (s[left_node] + add * left_len) % MOD
                lazy[left_node] = (lazy[left_node] + add) % MOD
                
                # Right child update
                right_node = 2 * node + 1
                right_len = r - mid
                sq[right_node] = (sq[right_node] + 2 * add * s[right_node] + add * add * right_len) % MOD
                s[right_node] = (s[right_node] + add * right_len) % MOD
                lazy[right_node] = (lazy[right_node] + add) % MOD
                
                lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                sq[node] = (sq[node] + 2 * val * s[node] + val * val * (r - l + 1)) % MOD
                s[node] = (s[node] + val * (r - l + 1)) % MOD
                lazy[node] = (lazy[node] + val) % MOD
                return
            push(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(2 * node, l, mid, ql, qr, val)
            if qr > mid:
                update(2 * node + 1, mid + 1, r, ql, qr, val)
            s[node] = (s[2 * node] + s[2 * node + 1]) % MOD
            sq[node] = (sq[2 * node] + sq[2 * node + 1]) % MOD

        ans = 0
        last_seen = {}
        
        for r_idx, x in enumerate(nums):
            l_idx = last_seen.get(x, -1) + 1
            update(1, 0, n - 1, l_idx, r_idx, 1)
            last_seen[x] = r_idx
            ans = (ans + sq[1]) % MOD
            
        return ans
