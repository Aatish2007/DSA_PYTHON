class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD=10**9+7
        last_added={}
        total=0
        for char in s:
            added=(total+1-last_added.get(char,0)) % MOD
            total=(total+added)% MOD
            last_added[char] = (last_added.get(char, 0) + added) % MOD
        return total
