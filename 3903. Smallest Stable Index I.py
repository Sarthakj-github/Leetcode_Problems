class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mn=[nums[-1]]
        n=len(nums)
        for i in range(n-2,-1,-1):
            mn.append(min(mn[-1],nums[i]))
        mn=mn[::-1]

        mx=nums[0]
        for i in range(n):
            mx=max(mx,nums[i])
            if (mx-mn[i])<=k:
                return i
        
        return -1
