class Solution:
    def minimumPushes(self, word: str) -> int:
        
        n=len(word)

        ans=0
        p=1
        while n>0:
            if n<8:
                ans+=n*p
            else:
                ans+=8*p
            p+=1
            n-=8
        return ans
