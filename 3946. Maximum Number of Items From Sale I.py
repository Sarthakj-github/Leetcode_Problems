class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        frees = [0] * n
        
        for i in range(n):
            f_i, _ = items[i]
            for j in range(n):
                if i != j:
                    f_j, _ = items[j]
                    if f_j % f_i == 0:
                        frees[i] += 1
                        
        dp = [0] * (budget + 1)
        
        for i in range(n):
            cost = items[i][1]
            free = frees[i]
            
            for b in range(budget, cost - 1, -1):
                dp[b] = max(dp[b], dp[b - cost] + 1 + free)
                
            for b in range(cost, budget + 1):
                dp[b] = max(dp[b], dp[b - cost] + 1)
                
        return dp[budget]
