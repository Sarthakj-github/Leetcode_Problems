class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        dp = [[(-1,0) for _ in range(n+1)] for _ in range(n+1)]
        dp[n-1][n-1] = (0,1)  # start at 'S'
        
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if board[i][j] == 'X': 
                    continue
                if board[i][j] not in 'SE':
                    val = int(board[i][j])
                else:
                    val = 0
                best, ways = -1, 0
                for x,y in [(i+1,j),(i,j+1),(i+1,j+1)]:
                    if x<n and y<n and dp[x][y][0] != -1:
                        score = dp[x][y][0] + val
                        if score > best:
                            best, ways = score, dp[x][y][1]
                        elif score == best:
                            ways = (ways + dp[x][y][1]) % MOD
                if best != -1:
                    dp[i][j] = (best, ways)
        
        return [dp[0][0][0] if dp[0][0][0]!=-1 else 0, dp[0][0][1]]
