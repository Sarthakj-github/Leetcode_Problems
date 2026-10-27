class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        
        grid=[['#' for _ in range(n)] for _ in range(m)]
        for i in range(m):
            grid[i][-1]='.'
        for j in range(n):
            grid[0][j]='.'
        
        ans=[]
        for k in grid:
            ans.append(''.join(k))
        
        return ans
