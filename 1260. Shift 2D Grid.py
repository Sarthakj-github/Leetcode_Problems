class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        l=m*n
        k%=l

        p=0
        seen=set()
        for i in range(l):
            if i not in seen:
                j=i
                v=-1
                while j not in seen:
                    seen.add(j)
                    v,grid[j//n][j%n]=grid[j//n][j%n],v
                    j=(j+k)%l
                grid[i//n][j%n]=v
        return grid
