class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        
        m=len(word)
        ans=0
        for p in patterns:
            n=len(p)
            for i in range(m):
                if p[0]==word[i]:
                    j,k=0,i
                    while j<n and k<m and p[j]==word[k]:
                        j+=1
                        k+=1
                    if j==n:
                        ans+=1
                        break
        return ans
