class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        l = len(restrictions)
        if l == 0:
            return n - 1
        if n == 1:
            return 0

        restrictions.sort()
        restrictions = [[1, 0]] + restrictions
        l += 1

        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])
            l += 1

        ans = 0
        # forward pass to adjust restrictions
        for i in range(l - 1):
            r1, h1 = restrictions[i]
            r2, h2 = restrictions[i + 1]
            restrictions[i + 1][1] = min(h2, h1 + (r2 - r1))

        # backward pass to adjust restrictions
        for i in range(l - 1, 0, -1):
            r1, h1 = restrictions[i]
            r2, h2 = restrictions[i - 1]
            restrictions[i - 1][1] = min(h2, h1 + (r1 - r2))

        # compute maximum possible height
        for i in range(l - 1):
            r1, h1 = restrictions[i]
            r2, h2 = restrictions[i + 1]
            ans = max(ans, (r2 - r1 + h1 + h2) // 2)

        return ans
