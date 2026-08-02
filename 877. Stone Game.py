class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        n=len(piles)
        d={}
        def trav(i,j,p):
            s=(-1)*p
            if i==j:
                return s*piles[i]
            
            if (i,j,p) not in d:
                d[(i,j,p)]=max(s*trav(i+1,j,p^1)+piles[i],s*trav(i,j-1,p^1)+piles[j])
            return d[(i,j,p)]
        
        return trav(0,n-1,0)>0
