class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stoneValue[i]
        
        @lru_cache(None)
        def f(l: int, r: int) -> int:
            if l == r:
                return 0
            ans = 0
            for m in range(l, r):
                Lsum = prefix[m+1] - prefix[l]
                Rsum = prefix[r+1] - prefix[m+1]
                
                if Lsum <= Rsum:
                    ans = max(ans, Lsum + f(l, m))
                if Lsum >= Rsum:
                    ans = max(ans, Rsum + f(m+1, r))
                
                if 2 * min(Lsum, Rsum) <= ans:
                    break
            return ans
        
        return f(0, n-1)
