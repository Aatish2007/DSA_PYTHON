'''
#BRUTE FORCE APPORACH
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
'''
#BETTER APPORACH USING STACK
class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        max_depth=0
        for char in s:
            if char=='(':
                stack.append(char)
                if len(stack)>max_depth:
                    max_depth=len(stack)
            elif char==')':
                stack.pop()
        return max_depth