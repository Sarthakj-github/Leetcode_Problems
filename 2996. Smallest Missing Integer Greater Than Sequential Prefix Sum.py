class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        
        n=len(nums)
        p=nums[0]
        i=1
        while i<n and nums[i]==(nums[i-1]+1):
            p+=nums[i]
            i+=1
        s=set(nums[i-1:n])
        while p in s:
            p+=1
        return p
