class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n=len(s)
        i=0
        ans=0
        d={}
        for j in range(n):
            if s[j] not in d:
                d[s[j]]=0
            d[s[j]]+=1
            if len(d)==3:
                p=i
                while i<j:
                    if d[s[i]]==1:
                        break
                    else:
                        d[s[i]]-=1
                        i+=1
                a,b=i-p+1,n-j
                print(p,i,j)
                ans+=(a*b)
                del d[s[i]]
                i+=1
        return ans
