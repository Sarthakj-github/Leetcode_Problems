class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        d={}
        for c in word:
            if c.islower():
                if c not in d:
                    d[c]=0
                elif d[c]==1:
                    d[c]=2
            else:
                cl=c.lower()
                if cl not in d:
                    d[cl]=2
                else:
                    d[cl]=max(1,d[cl])
        
        ans=0
        for c in d:
            if d[c]==1:
                ans+=1
        return ans
