class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        
        def lcm(a, b):
            return a // gcd(a, b) * b
        
        def count(x):
            total = 0
            n = len(coins)
            for r in range(1, n+1):
                for comb in combinations(coins, r):
                    l = comb[0]
                    for c in comb[1:]:
                        l = lcm(l, c)
                        if l > x:
                            break
                    else:
                        if r % 2:
                            total += x // l
                        else:
                            total -= x // l
            return total
        
        i, j = min(coins), min(coins) * k
        ans = -1
        while i <= j:
            m = (i + j) // 2
            n = count(m)
            if n >= k:
                ans = m
                j = m - 1
            else:
                i = m + 1
        return ans
