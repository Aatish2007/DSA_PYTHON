"""
from itertools import combinations

class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        m, n = len(word1), len(word2)
        for indices in combinations(range(m), n):
            mismatches = 0
            for k in range(n):
                if word1[indices[k]] != word2[k]:
                    mismatches += 1
                    if mismatches > 1:
                        break
            if mismatches <= 1:
                return list(indices)  
                
        return []
"""
#better Apporach
class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        m, n = len(word1), len(word2)
        last = [-1] * n
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1
            
        ans = []
        can_skip = True  
        j = 0
        for i in range(m):
            if j == n:
                break
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif can_skip and (j == n - 1 or last[j + 1] > i):
                can_skip = False
                ans.append(i)
                j += 1
                
        return ans if len(ans) == n else []