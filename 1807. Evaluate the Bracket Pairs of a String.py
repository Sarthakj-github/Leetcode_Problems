class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d={}

        for k,v in knowledge:
            d[k]=v
        
        i=0
        n=len(s)
        ns=''
        while i<n:
            if s[i]=='(':
                j=i+1
                p=''
                while j<n and s[j]!=')':
                    p+=s[j]
                    j+=1
                if p in d:
                    ns+=d[p]
                else:
                    ns+='?'
                i=j+1
            else:
                ns+=s[i]
                i+=1
        return ns
