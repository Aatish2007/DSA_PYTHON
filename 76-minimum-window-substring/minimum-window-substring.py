from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}

        have = 0
        need_count = len(need)

        left = 0
        result = [-1, -1]
        min_len = float("inf")

        for right in range(len(s)):

            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == need_count:

                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    result = [left, right]

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        left, right = result

        if min_len == float("inf"):
            return ""

        return s[left:right + 1]