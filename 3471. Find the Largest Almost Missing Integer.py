class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        d={}
        n=len(nums)
        for i in range(n-k+1):
            for j in range(i,i+k):
                if nums[j] not in d:
                    d[nums[j]]=set()
                d[nums[j]].add(i)
        ans=-1
        for i in d:
            if len(d[i])==1:
                ans=max(ans,i)
        return ans
