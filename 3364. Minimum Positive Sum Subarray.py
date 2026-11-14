class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        ans=float('inf')
        for i in range(n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                if l<=(j-i+1)<=r and s>0:
                    ans=min(ans,s)
        if ans==float('inf'):
            ans=-1
        return ans
