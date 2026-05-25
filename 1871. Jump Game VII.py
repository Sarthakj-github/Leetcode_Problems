class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        if s[-1]=='1':
            return False
        n=len(s)
        Q=[0]
        vis=set([0])
        m=0
        while Q!=[]:
            i=Q.pop(0)
            if i==(n-1):
                return True
            for j in range(max(m,i+minJump),min(i+maxJump+1,n)):
                if s[j]=='0' and j not in vis:
                    Q.append(j)
                    vis.add(j)
            m=min(i+maxJump+1,n)
        return False
