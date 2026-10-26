class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        vis=set()
        m,n=len(grid),len(grid[0])

        def trav(x,y):
            if x<0 or x==m or y<0 or y==n:
                return 0

            if (x,y) in vis:
                return 0

            if grid[x][y]==0:
                return 0

            vis.add((x,y))

            ans=grid[x][y]

            L=[(x,y+1),(x+1,y),(x-1,y),(x,y-1)]

            for p,q in L:
                ans += trav(p,q)

            return ans

        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i,j) not in vis:
                    if trav(i,j) % k == 0:
                        ans += 1

        return ans
