class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:

        n=len(arr)
        D={}
        def trav(i):
            if i not in D:
                a,b=max(0,i-d),min(i+d,n-1)
                ans=0
                p,q=i-1,i+1
                while a<=p and arr[p]<arr[i]:
                    ans=max(ans,trav(p))
                    p-=1
                while q<=b and arr[i]>arr[q]:
                    ans=max(ans,trav(q))
                    q+=1
                D[i]=ans+1
            return D[i]

        res=1
        for i in range(n):
            res=max(res,trav(i))
        print(D)
        return res
