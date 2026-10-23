class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        
        n=len(nums)
        k=None
        for i in range(n):
            if nums[i]!=i:
                if k==None:
                    k=nums[i]
                else:
                    k&=nums[i]
        if k==None:
            return 0
        return k
