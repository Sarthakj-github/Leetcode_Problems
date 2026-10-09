class Solution:
    def minInsertions(self, s: str) -> int:
        S = []
        ans = 0
        n = len(s)
        i = 0

        while i < n:
            if s[i] == '(':
                S.append(i)
            else:
                if S:
                    S.pop()
                else:
                    ans += 1
                if i + 1 == n or s[i + 1] == '(':
                    ans += 1
                else:
                    i += 1
            i += 1
        ans += len(S) * 2
        return ans
