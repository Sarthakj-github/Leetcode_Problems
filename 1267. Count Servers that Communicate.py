class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        M=[0 for _ in range(m)]
        N=[0 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    M[i]+=1
                    N[j]+=1
        
        ans=sum(M)
        for i in range(m):
            for j in range(n):
                if grid[i][j] and M[i]==N[j]==1:
                    ans-=1
        return ans
