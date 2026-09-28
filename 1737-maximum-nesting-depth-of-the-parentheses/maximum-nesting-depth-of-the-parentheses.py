class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth=0
        n=len(s)
        for i in range(n):
            if s[i]=='(':
                curr_depth=0
                for j in range(i,n):
                    if s[j]=='(':
                        curr_depth+=1
                    elif s[j]==')':
                        curr_depth-=1
                    if curr_depth>max_depth:
                        max_depth=curr_depth
        return max_depth