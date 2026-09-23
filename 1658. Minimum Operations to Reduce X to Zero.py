class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n=len(nums)
        l,r=[],[]
        m=n+1
        for i in range(n):
            if l==[]:
                l.append(nums[i])
            else:
                l.append(l[-1]+nums[i])
            if r==[]:
                r.append(nums[n-i-1])
            else:
                r.append(r[-1]+nums[n-i-1])
            if l[-1]==x:
                m=min(m,i+1)
            if r[-1]==x:
                m=min(m,i+1)

        i=0
        while i<n and l[i]<x:
            a,b=0,n-1
            while a<=b:
                p=(a+b)//2
                if r[p]==(x-l[i]):
                    m=min(m,i+1+p+1)
                    break
                elif r[p]<(x-l[i]):
                    a=p+1
                else:
                    b=p-1
            i+=1
        if m>n:
            return -1
        return m
