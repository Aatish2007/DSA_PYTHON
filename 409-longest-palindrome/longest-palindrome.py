from collections import Counter


class Solution:

    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        # Sum up even parts of each count
        length = sum(count // 2 * 2 for count in counts.values())

        # If the palindrome length is less than the string length,
        # it means at least one character had an odd count to fill the middle spot.
        return length + (1 if length < len(s) else 0)