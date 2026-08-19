class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        d={}
        for r,s in reservedSeats:
            if r not in d:
                d[r]=set()
            d[r].add(s)
        
        ans=0
        for r in d:
            for i in [2,4,6]:
                j=i
                f=1
                for j in range(i,i+4):
                    if j in d[r]:
                        f=0
                        break
                    else:
                        d[r].add(j)
                if f:
                    ans+=1
        l=n-len(d)
        return ans+l*2
