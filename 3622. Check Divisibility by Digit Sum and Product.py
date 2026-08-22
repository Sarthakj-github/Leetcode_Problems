class Solution:
    def checkDivisibility(self, n: int) -> bool:
        
        a,b=0,1
        for i in str(n):
            a+=int(i)
            b*=int(i)
        
        return (n%(a+b))==0
