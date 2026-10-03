class Solution:
    def longestValidParentheses(self, s: str) -> int:
        S=[-1]
        n=len(s)
        m=0
        for i in range(n):
            if s[i]=='(':
                S.append(i)
            else:
                S.pop()
                if S==[]:
                    S.append(i)
                else:
                    m=max(m,i-S[-1])
        return m
