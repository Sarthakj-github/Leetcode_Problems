class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        
        vis=set()
        m,n=len(grid),len(grid[0])

        def trav(x,y):
            if x<0 or x==m or y<0 or y==n:
                return False

            if (x,y) in vis:
                return True

            if grid[x][y]:
                return True

            vis.add((x,y))

            L=[(x,y+1),(x+1,y),(x-1,y),(x,y-1)]

            ans=True
            for p,q in L:
                ans &= trav(p,q)

            return ans

        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0 and (i,j) not in vis:
                    if trav(i,j):
                        ans+=1

        return ans
