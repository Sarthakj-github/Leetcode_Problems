class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = defaultdict(list)
        indeg = [0]*n
        maxCost = 0

        for u,v,c in edges:
            if online[u] and online[v]:
                g[u].append((v,c))
                indeg[v]+=1
                maxCost = max(maxCost,c)

        # Topological order
        topo=[]
        q=deque([i for i in range(n) if indeg[i]==0])
        while q:
            u=q.popleft()
            topo.append(u)
            for v,c in g[u]:
                indeg[v]-=1
                if indeg[v]==0:
                    q.append(v)

        def can(mid:int)->bool:
            dp=[float("inf")]*n
            dp[0]=0
            for u in topo:
                if dp[u]==float("inf"): continue
                for v,c in g[u]:
                    if c>=mid and dp[u]+c<dp[v]:
                        dp[v]=dp[u]+c
            return dp[n-1]<=k

        lo,hi=0,maxCost
        ans=-1
        while lo<=hi:
            mid=(lo+hi)//2
            if can(mid):
                ans=mid
                lo=mid+1
            else:
                hi=mid-1
        return ans
