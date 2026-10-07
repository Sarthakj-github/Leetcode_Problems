class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        lrem = rrem = 0
        for ch in s:
            if ch == '(':
                lrem += 1
            elif ch == ')':
                if lrem > 0:
                    lrem -= 1
                else:
                    rrem += 1

        ans = set()

        def dfs(i, path, bal, lrem, rrem):
            if i == len(s):
                if lrem == 0 and rrem == 0 and bal == 0:
                    ans.add(path)
                return

            ch = s[i]

            if ch == '(' and lrem > 0:
                dfs(i + 1, path, bal, lrem - 1, rrem)
            elif ch == ')' and rrem > 0:
                dfs(i + 1, path, bal, lrem, rrem - 1)

            if ch not in '()':
                dfs(i + 1, path + ch, bal, lrem, rrem)
            elif ch == '(':
                dfs(i + 1, path + ch, bal + 1, lrem, rrem)
            elif ch == ')' and bal > 0:
                dfs(i + 1, path + ch, bal - 1, lrem, rrem)

        dfs(0, '', 0, lrem, rrem)
        return list(ans)
