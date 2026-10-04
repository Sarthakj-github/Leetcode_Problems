class Solution:
    def checkValidString(self, s: str) -> bool:
        
        n=len(s)
        d={}
        def trav(i,p):
            if p<0:
                return False
            if i==n:
                return p==0
            else:
                if (i,p) not in d:
                    if s[i]=='(':
                        d[(i,p)]=trav(i+1,p+1)
                    elif s[i]==')':
                        d[(i,p)]=trav(i+1,p-1)
                    else:
                        d[(i,p)]=trav(i+1,p+1) or trav(i+1,p-1) or trav(i+1,p)
                return d[(i,p)]
        return trav(0,0)
