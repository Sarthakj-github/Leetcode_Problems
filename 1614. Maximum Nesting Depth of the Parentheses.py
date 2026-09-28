class Solution:
    def maxDepth(self, s: str) -> int:
        
        m=c=0
        for i in s:
            if c>m:
                m=c
            if i=='(':
                c+=1
            elif i==')':
                c-=1
        return m
