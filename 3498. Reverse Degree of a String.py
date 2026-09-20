class Solution:
    def reverseDegree(self, s: str) -> int:
        
        n=len(s)
        ans=0
        for i in range(n):
            ans+=(123-ord(s[i]))*(i+1)
        
        return ans
