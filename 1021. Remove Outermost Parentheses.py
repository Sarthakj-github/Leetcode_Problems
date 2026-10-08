class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        L=''
        S=[]
        n=len(s)
        for i in range(n):
            if s[i]=='(':
                S.append(i)
            else:
                if len(S)==1:
                    L+=s[S.pop()+1:i]
                else:
                    S.pop()
        return L
