class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        
        if num*9<sum:
            return ""
        
        s=''
        while num:
            p=min(sum,9)
            sum-=p
            s+=str(p)
            num-=1
        return s
