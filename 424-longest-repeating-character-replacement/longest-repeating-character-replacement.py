'''
BRUTEFORCE APPROACH
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        n = len(s)

        for left in range(n):
            freq = {}

            for right in range(left, n):
                char = s[right]
                freq[char] = freq.get(char, 0) + 1

                most_frequent = max(freq.values())
                window_length = right - left + 1
                replacements_needed = window_length - most_frequent

                if replacements_needed <= k:
                    max_length = max(max_length, window_length)

        return max_length
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        max_frequency = 0
        freq = {}

        for right in range(len(s)):
            char = s[right]
            freq[char] = freq.get(char, 0) + 1

            max_frequency = max(max_frequency, freq[char])

            window_length = right - left + 1

            if window_length - max_frequency > k:
                left_char = s[left]
                freq[left_char] -= 1
                left += 1
            else:
                max_length = max(max_length, window_length)

        return max_length