class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)

        d={}
        for x in word:
            if x not in d:
                d[x]=0
            d[x]+=1
        
        H=[d[x] for x in d]
        H.sort()

        p,q=1,1
        ans=0

        while H:
            a=H.pop()
            ans+=a*q
            p+=1
            if p==9:
                q+=1
                p=1
        
        return ans
