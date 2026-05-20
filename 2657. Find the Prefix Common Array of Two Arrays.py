class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        d=defaultdict(int)
        ans=0
        res=[]
        for a,b in zip(A,B):
            d[a]+=1
            d[b]+=1
            if a==b:
                ans+=1
            else:
                if d[a]==2:
                    ans+=1
                if d[b]==2:
                    ans+=1
            res.append(ans)
        return res
