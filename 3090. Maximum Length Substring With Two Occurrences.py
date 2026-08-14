class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        d={}
        n=len(s)
        i=0
        ans=1
        for j in range(n):
            a=s[j]
            if a not in d:
                d[a]=[]
            if len(d[a])==2:
                i=max(i,d[a].pop(0)+1)
            d[a].append(j)
            ans=max(ans,j-i+1)
            print(d,i,j)
        return ans
