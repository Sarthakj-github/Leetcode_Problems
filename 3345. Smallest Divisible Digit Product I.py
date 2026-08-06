class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        while True:
            s=1
            for i in str(n):
                s*=int(i)
            if s%t==0:
                return n
            n+=1
