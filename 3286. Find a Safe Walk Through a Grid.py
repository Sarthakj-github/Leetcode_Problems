class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        L = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        
        queue = deque([(0, 0, health - grid[0][0])])
        visited = [[-1] * n for _ in range(m)]
        visited[0][0] = health - grid[0][0]
        
        while queue:
            i, j, h = queue.popleft()
            
            if h <= 0:
                continue
            
            if i == m - 1 and j == n - 1:
                return True
            
            for a, b in L:
                p, q = i + a, j + b
                if 0 <= p < m and 0 <= q < n:
                    new_health = h - grid[p][q]
                    if new_health > visited[p][q]:
                        visited[p][q] = new_health
                        queue.append((p, q, new_health))
        
        return False
