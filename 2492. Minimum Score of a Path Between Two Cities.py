class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        D={}
        for a,b,d in roads:
            if a not in D:
                D[a]=set()
            D[a].add((b,d))
            if b not in D:
                D[b]=set()
            D[b].add((a,d))
        vis=set()
        Q=[1]
        ans=float('inf')
        while Q:
            a=Q.pop(0)
            vis.add(a)
            if a in D:
                for b,d in D[a]:
                    if b not in vis:
                        Q.append(b)
                        ans=min(ans,d)
        return ans
