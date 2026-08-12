'''
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_someone=0
        trusted_by=n-1
        trust_someone=[0]*(n+1)
        trusted_by=[0]*(n+1)
        for a,b in trust:
            trust_someone [a] +=1
            trusted_by [b] +=1
        for i in range (1,n+1):
            if trust_someone[i]==0 and trusted_by[i]==n-1:
                return i
        return -1
'''
#optimal Approach
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        score=[0]*(n+1)
        for a,b in trust:
            score[a]-=1
            score[b]+=1
        for i in range(1,n+1):
            if score[i]==n-1:
                return i
        return -1