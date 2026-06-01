class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
        n=len(cost)
        cost.sort(reverse=True)
        ans=0
        for i in range(0,n,3):
            ans+=cost[i]
            if (i+1)<n:
                ans+=cost[i+1]
        return ans
