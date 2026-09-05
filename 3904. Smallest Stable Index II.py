class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        n=len(nums)
        L=[nums[-1]]
        for i in range(n-2,-1,-1):
            L.append(min(L[-1],nums[i]))
        L=L[::-1]

        mx=nums[0]
        for i in range(n):
            mx=max(nums[i],mx)
            if (mx-L[i])<=k:
                return i
        return -1
