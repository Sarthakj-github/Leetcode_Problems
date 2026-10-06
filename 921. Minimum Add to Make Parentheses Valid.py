class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        S=[]
        for i in s:
            if S!=[] and S[-1]=='(' and i==')':
                S.pop()
            else:
                S.append(i)
        return len(S)
