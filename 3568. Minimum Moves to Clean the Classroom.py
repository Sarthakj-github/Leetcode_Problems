class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter_positions = []
        start = None
        
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'L':
                    litter_positions.append((i, j))
                elif classroom[i][j] == 'S':
                    start = (i, j)
        
        k = len(litter_positions)
        litter_index = {pos: idx for idx, pos in enumerate(litter_positions)}
        
        q = deque()
        q.append((start[0], start[1], energy, 0, 0))
        seen = set()
        seen.add((start[0], start[1], energy, 0))
        
        while q:
            i, j, e, mask, moves = q.popleft()
            if mask == (1 << k) - 1:
                return moves
            
            for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n and classroom[ni][nj] != 'X':
                    ne = e - 1
                    if ne < 0:
                        continue
                    nmask = mask
                    if classroom[ni][nj] == 'R':
                        ne = energy
                    elif classroom[ni][nj] == 'L':
                        nmask |= 1 << litter_index[(ni, nj)]
                    
                    state = (ni, nj, ne, nmask)
                    if state not in seen:
                        seen.add(state)
                        q.append((ni, nj, ne, nmask, moves+1))
        
        return -1
