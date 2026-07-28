class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        d={}
        ns=''
        p=''
        for i in s:
            if i not in d:
                d[i]=0
            d[i]+=1
            if d[i]%2:
                p=i
        
        if d[p]%2==0:
            p=''
        
        for i in sorted(d.keys()):
            ns+=i*(d[i]//2)
        
        return ns+p+ns[::-1]
