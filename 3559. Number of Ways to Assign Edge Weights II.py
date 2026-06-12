class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 1000000007
        n = len(edges) + 1
        LOG = math.ceil(math.log2(n)) + 1

        # adjacency
        d = [[] for _ in range(n+1)]
        for u, v in edges:
            d[u].append(v)
            d[v].append(u)

        dep = [0]*(n+1)
        up = [[-1]*(LOG) for _ in range(n+1)]

        def dfs(u, p):
            up[u][0] = p
            for j in range(1, LOG):
                if up[u][j-1] != -1:
                    up[u][j] = up[up[u][j-1]][j-1]
            for v in d[u]:
                if v != p:
                    dep[v] = dep[u] + 1
                    dfs(v, u)

        dfs(1, -1)

        def lca(u, v):
            if dep[u] < dep[v]:
                u, v = v, u
            # lift u
            diff = dep[u] - dep[v]
            for j in range(LOG):
                if diff & (1<<j):
                    u = up[u][j]
            if u == v:
                return u
            for j in reversed(range(LOG)):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]

        ans = []
        for a, b in queries:
            cp = lca(a, b)
            v = dep[a] + dep[b] - 2*dep[cp]
            ans.append(pow(2, v-1, MOD) if v else 0)
        return ans
