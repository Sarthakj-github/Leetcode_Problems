class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx=max(nums)
        freq=[0]*(mx+1)
        for x in nums: freq[x]+=1
        
        cnt=[0]*(mx+1)
        for g in range(1,mx+1):
            for m in range(g,mx+1,g):
                cnt[g]+=freq[m]
        
        pairs=[0]*(mx+1)
        for g in range(mx,0,-1):
            if cnt[g]>=2:
                pairs[g]=cnt[g]*(cnt[g]-1)//2
            for m in range(2*g,mx+1,g):
                pairs[g]-=pairs[m]
        
        # prefix sums of counts
        prefix=[]
        total=0
        for g in range(1,mx+1):
            if pairs[g]:
                total+=pairs[g]
                prefix.append((total,g))
        
        ans=[]
        for q in queries:
            # binary search in prefix
            lo,hi=0,len(prefix)-1
            while lo<hi:
                mid=(lo+hi)//2
                if prefix[mid][0]>q: hi=mid
                else: lo=mid+1
            ans.append(prefix[lo][1])
        return ans
