class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        dp = [[0, 0] for _ in range(n + 1)]
        dp[1] = [1, 1]
        for r in range(m):
            for c in range(n):
                col = c + 1
                if grid[r][c] == 1:
                    dp[col] = [dp[col][1], dp[col-1][0]]
                else:
                    val = (dp[col][1] + dp[col-1][0]) % MOD
                    dp[col] = [val, val]
                    
        return dp[n][0]
