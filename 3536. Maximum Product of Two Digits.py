class Solution:
    def maxProduct(self, n: int) -> int:
        a,b=-1,-1

        while n:
            k=n%10
            if k>a:
                a,b=k,a
            elif k>b:
                b=k
            n//=10
        
        return a*b
