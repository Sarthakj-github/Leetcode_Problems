class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n=len(nums)

        import math
        log=[0]*(n+1)
        for i in range(2,n+1):
            log[i]=log[i//2]+1
        K=log[n]+1
        st_max=[[0]*n for _ in range(K)]
        st_min=[[0]*n for _ in range(K)]
        for i in range(n):
            st_max[0][i]=nums[i]
            st_min[0][i]=nums[i]
        for j in range(1,K):
            for i in range(n-(1<<j)+1):
                st_max[j][i]=max(st_max[j-1][i],st_max[j-1][i+(1<<(j-1))])
                st_min[j][i]=min(st_min[j-1][i],st_min[j-1][i+(1<<(j-1))])

        def query(l,r):
            j=log[r-l+1]
            mx=max(st_max[j][l],st_max[j][r-(1<<j)+1])
            mn=min(st_min[j][l],st_min[j][r-(1<<j)+1])
            return mx-mn

        heap=[(-query(i,n-1),i,n-1) for i in range(n)]
        heapq.heapify(heap)

        ans=0
        for _ in range(k):
            val,l,r=heapq.heappop(heap)
            ans+=-val
            if r>l:
                heapq.heappush(heap,(-query(l,r-1),l,r-1))
        return ans
