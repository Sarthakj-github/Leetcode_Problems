class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon={'b':1,'a':1,'l':2,'o':2,'n':1}
        d={'b':0,'a':0,'l':0,'o':0,'n':0}
        for t in text:
            if t in d:
                d[t]+=1
        ans=len(text)
        for k in balloon:
            ans=min(ans,d[k]//balloon[k])
        return ans
