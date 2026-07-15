class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        
        a=n**2
        b=a+n

        def gcd(i,j):
            if j==0:
                return i
            return gcd(j,i%j)
        
        return gcd(a,b)
