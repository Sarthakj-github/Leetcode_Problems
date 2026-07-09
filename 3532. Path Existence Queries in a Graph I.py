class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        d = [-1] * n
        E = [(nums[i], i) for i in range(n)]
        E.sort()

        for x in range(n):
            k, p = E[x]
            i, j = x, n - 1
            ans = -1
            while i <= j:
                m = (i + j) // 2
                v = abs(E[m][0] - k)
                if v <= maxDiff:
                    ans = E[m][1]
                    i = m + 1
                else:
                    j = m - 1
            if ans != -1 and ans != p:
                a, b = sorted([p, ans])
                d[a] = b

        ans = []
        for i, j in queries:
            res = False
            while True:
                if i == j:
                    res = True
                    break
                elif d[i] == -1 and d[j] == -1:
                    break
                if d[i] != -1:
                    i = d[i]
                if d[j] != -1:
                    j = d[j]
            ans.append(res)
        return ans
