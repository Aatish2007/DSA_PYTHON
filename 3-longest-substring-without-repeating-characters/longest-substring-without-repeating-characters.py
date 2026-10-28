'''
BRUTEFORCE APPORACH
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=0
        n=len(s)
        for start in range(n):
            seen=set()
            for end in range(start,n):
                if s[end] in seen :
                    break
                seen.add(s[end])
                max_length=max(max_length,end-start+1)
        return max_length

#BETTER APPORACH USING SLIDING WINDOW +SET
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]

            if char in last_seen:
                left = max(left, last_seen[char] + 1)

            last_seen[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length