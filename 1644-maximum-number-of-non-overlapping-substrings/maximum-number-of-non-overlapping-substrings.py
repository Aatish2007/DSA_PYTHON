class Solution:

    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []

        for ch in first:
            l = first[ch]
            r = last[ch]
            valid = True

            i = l
            while i <= r:
                r = max(r, last[s[i]])
                if first[s[i]] < l:
                    valid = False
                    break
                i += 1

            if valid:
                intervals.append((r, l))

        intervals.sort()
        res = []
        prev_end = -1

        for r, l in intervals:
            if l > prev_end:
                res.append(s[l : r + 1])
                prev_end = r

        return res