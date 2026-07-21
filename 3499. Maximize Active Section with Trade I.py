class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        s = '1' + s + '1'

        ans = 0
        c = 0
        L = []
        for i in range(n, 0, -1):
            if s[i] == '0':
                c += 1
            else:
                c = 0
                ans += 1
            L.append(c)
        L.reverse()

        cz = 0
        i = 1
        res = 0
        while i <= n:
            if s[i] == '1' and s[i-1] == '0':
                j = i + 1
                while j <= n and s[j] == '1':
                    j += 1
                if j <= n:
                    res = max(res, L[j-1] + cz)
                i = j - 1
                cz = 0
            elif s[i] == '0':
                cz += 1
            i += 1
        return ans + res
