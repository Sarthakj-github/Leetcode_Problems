class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        
        if (cost1+cost2)<=costBoth:
            return need1*cost1+need2*cost2
        
        m=min(need1,need2)
        need1-=m
        need2-=m
        if need1:
            return m*costBoth+min(costBoth,cost1)*need1
        return m*costBoth+min(costBoth,cost2)*need2
