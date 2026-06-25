class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        
        n=len(nums)
        res=0

        for i in range(n):
            c,p=0,0
            for j in range(i,n):
                if nums[j]==target:
                    c+=1
                p+=1
                if (p-c)<c:
                    res+=1
        
        return res
