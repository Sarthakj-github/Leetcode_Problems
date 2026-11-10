class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        
        costs=[0]+costs
        d={}
        def trav(i):
            if i==n:
                return 0
            if i not in d:
                ans=float('inf')
                if (i+1)<=n:
                    ans=min(ans,trav(i+1)+costs[i+1]+1)
                if(i+2)<=n:
                    ans=min(ans,trav(i+2)+costs[i+2]+4)
                if(i+3)<=n:
                    ans=min(ans,trav(i+3)+costs[i+3]+9)
                d[i]=ans
            return d[i]
        
        return trav(0)
