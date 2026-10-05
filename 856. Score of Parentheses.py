class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        S=[]
        for i in s:
            if i=='(':
                S.append(0)
            else:
                s=0
                while S[-1]:
                    s+=S.pop()
                S.pop()
                if s:
                    S.append(s*2)
                else:
                    S.append(1)

        return sum(S)
