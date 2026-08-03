class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        n = len(stoneValue)
        d = {}
        
        def trav(i):
            if i >= n:
                return 0
            if i not in d:
                best = float('-inf')
                total = 0
                for k in range(3):
                    if i + k < n:
                        total += stoneValue[i + k]
                        best = max(best, total - trav(i + k + 1))
                d[i] = best
            return d[i]
        
        res = trav(0)
        if res == 0:
            return "Tie"
        elif res > 0:
            return "Alice"
        else:
            return "Bob"
