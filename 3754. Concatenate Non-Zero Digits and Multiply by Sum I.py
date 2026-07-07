class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x,sum=0,0
        p=1
        while n:
            i=n%10
            if i:
                x+=i*p
                sum+=i
                p*=10
            n//=10
        return x*sum
