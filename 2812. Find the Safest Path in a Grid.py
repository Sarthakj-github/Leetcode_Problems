class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        sm = [[-1]*n for _ in range(n)]

        # multi-source BFS to fill sm with distance to nearest thief
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    sm[i][j] = 0
                    q.append((i, j))
        while q:
            x, y = q.popleft()
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n and sm[nx][ny] == -1:
                    sm[nx][ny] = sm[x][y] + 1
                    q.append((nx, ny))

        # binary search + BFS to check path
        def can(mid):
            if sm[0][0] < mid:
                return False
            vis = [[False]*n for _ in range(n)]
            dq = deque([(0,0)])
            vis[0][0] = True
            while dq:
                i,j = dq.popleft()
                if i == n-1 and j == n-1:
                    return True
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    a,b = i+dx,j+dy
                    if 0 <= a < n and 0 <= b < n and not vis[a][b] and sm[a][b] >= mid:
                        vis[a][b] = True
                        dq.append((a,b))
            return False

        lo, hi, ans = 0, n*2, 0
        while lo <= hi:
            mid = (lo+hi)//2
            if can(mid):
                ans = mid
                lo = mid+1
            else:
                hi = mid-1
        return ans
