class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        s = list(s)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = n.bit_length()
        up = [[-1] * LOG for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0
        
        initial_mask = [0] * n

        def dfs(u, p, d, current_mask):
            nonlocal timer
            depth[u] = d
            up[u][0] = p
            for j in range(1, LOG):
                if up[u][j-1] != -1:
                    up[u][j] = up[up[u][j-1]][j-1]
            
            tin[u] = timer
            timer += 1
            
            current_mask ^= (1 << (ord(s[u]) - ord('a')))
            initial_mask[u] = current_mask
            
            for v in adj[u]:
                if v != p:
                    dfs(v, u, d + 1, current_mask)
            tout[u] = timer - 1

        dfs(0, -1, 0, 0)

        bit = [0] * (n + 2)

        def update(idx, val):
            idx += 1
            while idx < len(bit):
                bit[idx] ^= val
                idx += idx & (-idx)

        def range_update(l, r, val):
            update(l, val)
            update(r + 1, val)

        def point_query(idx):
            idx += 1
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        for i in range(n):
            if initial_mask[i] != 0:
                range_update(tin[i], tin[i], initial_mask[i])

        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for j in range(LOG - 1, -1, -1):
                if depth[u] - (1 << j) >= depth[v]:
                    u = up[u][j]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != -1 and up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == 'query':
                u, v = int(parts[1]), int(parts[2])
                lca = get_lca(u, v)
                mask_u = point_query(tin[u])
                mask_v = point_query(tin[v])
                lca_char_mask = 1 << (ord(s[lca]) - ord('a'))
                path_mask = mask_u ^ mask_v ^ lca_char_mask
                ans.append(path_mask.bit_count() <= 1)
            else:
                u = int(parts[1])
                new_char = parts[2]
                old_char = s[u]
                if old_char != new_char:
                    s[u] = new_char
                    delta = (1 << (ord(old_char) - ord('a'))) ^ (1 << (ord(new_char) - ord('a')))
                    range_update(tin[u], tout[u], delta)

        return ans
