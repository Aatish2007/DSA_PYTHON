class SegmentNode:

    def __init__(self, l: int, r: int):
        self.l = l
        self.r = r
        self.length = r - l + 1
        self.max_len = 1
        self.prefix_len = 1
        self.suffix_len = 1
        self.left_char = ""
        self.right_char = ""


class Solution:

    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: list[int]
    ) -> list[int]:
        s_list = list(s)
        n = len(s)
        tree = [None] * (4 * n)

        def merge(
            node: SegmentNode, left: SegmentNode, right: SegmentNode
        ) -> None:
            node.left_char = left.left_char
            node.right_char = right.right_char

            # Base max length is the max of both child subtrees
            node.max_len = max(left.max_len, right.max_len)

            # Prefix length logic
            node.prefix_len = left.prefix_len
            if (
                left.prefix_len == left.length
                and left.right_char == right.left_char
            ):
                node.prefix_len += right.prefix_len

            # Suffix length logic
            node.suffix_len = right.suffix_len
            if (
                right.suffix_len == right.length
                and left.right_char == right.left_char
            ):
                node.suffix_len += left.suffix_len

            # Boundary match in the middle
            if left.right_char == right.left_char:
                node.max_len = max(
                    node.max_len, left.suffix_len + right.prefix_len
                )

        def build(idx: int, l: int, r: int) -> None:
            node = SegmentNode(l, r)
            tree[idx] = node

            if l == r:
                node.left_char = s_list[l]
                node.right_char = s_list[l]
                return

            mid = (l + r) // 2
            build(2 * idx, l, mid)
            build(2 * idx + 1, mid + 1, r)
            merge(node, tree[2 * idx], tree[2 * idx + 1])

        def update(idx: int, l: int, r: int, target_i: int, ch: str) -> None:
            if l == r:
                node = tree[idx]
                node.left_char = ch
                node.right_char = ch
                s_list[target_i] = ch
                return

            mid = (l + r) // 2
            if target_i <= mid:
                update(2 * idx, l, mid, target_i, ch)
            else:
                update(2 * idx + 1, mid + 1, r, target_i, ch)

            merge(tree[idx], tree[2 * idx], tree[2 * idx + 1])

        # 1. Build the initial segment tree
        build(1, 0, n - 1)

        # 2. Process queries
        ans = []
        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(tree[1].max_len)

        return ans