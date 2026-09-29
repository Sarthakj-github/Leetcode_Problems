class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == ')' or grid[-1][-1] == '(':
            return False

        # (i, j, balance)
        Q = deque([(0, 0, 1)])
        vis = {(0, 0, 1)}

        while Q:
            i, j, s = Q.popleft()
            if i == m - 1 and j == n - 1 and s == 0:
                return True
            for ni, nj in ((i + 1, j), (i, j + 1)):
                if ni < m and nj < n:
                    ns = s + (1 if grid[ni][nj] == '(' else -1)
                    if ns >= 0 and (ni, nj, ns) not in vis:
                        vis.add((ni, nj, ns))
                        Q.append((ni, nj, ns))
        return False
