class Solution:
    def digitSum(self, s: str, k: int) -> str:
        

        def make_sum(l):
            sm=0
            for a in l:
                sm+=int(a)
            return sm
            
        n=len(s)
        while n>k:
            ns=''
            for i in range(0,n,k):
                ns+=str(make_sum(s[i:i+k]))
            s=ns
            n=len(s)
        
        return s
