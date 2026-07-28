class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        d={}
        ns=''
        p=''
        n=len(s)
        if n%2:
            p=s[n//2]
        for i in range(n//2):
            if s[i] not in d:
                d[s[i]]=0
            d[s[i]]+=1
            
        for i in sorted(d.keys()):
            ns+=i*(d[i])
        
        return ns+p+ns[::-1]
