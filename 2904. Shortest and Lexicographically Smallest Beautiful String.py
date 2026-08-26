class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n=len(s)
        c,i,j=0,0,0
        ans=[]
        m=float("inf")
        while j<n:
            if s[j]=='1':
                c+=1
            if c==k:
                ans.append(s[i:j+1])
                m=min(m,j-i+1)
                i+=1
                c-=1
            while i<=j and s[i]=='0':
                i+=1
            j+=1
        if ans==[]:
            return ''
        L=[]
        for i in ans:
            if len(i)==m:
                L.append(i)
        return sorted(L)[0]
