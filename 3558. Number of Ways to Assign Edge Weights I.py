class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        if len(edges) == 1:
            return 1
        MOD=1000000007
        d = {}
        for u, v in edges:
            d.setdefault(u, []).append(v)
            d.setdefault(v, []).append(u)

        dep = {}
        def trav(i, r, parent):
            dep[i] = r
            for j in d.get(i, []):
                if j != parent:
                    trav(j, r + 1, i)

        trav(1, 0, -1)

        m = max(dep.values())
        return pow(2, m - 1, MOD)
