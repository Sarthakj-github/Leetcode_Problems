class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        ans=0
        for n in range(num1,num2+1):
            s=str(n)
            l=len(s)
            for i in range(1,l-1):
                if s[i-1]<s[i]>s[i+1] or s[i-1]>s[i]<s[i+1]:
                    ans+=1
        return ans
