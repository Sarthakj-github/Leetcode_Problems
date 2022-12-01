class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        f=0
        l=len(nums)-1
        m=0
        while m<=l:
            if nums[m]==0:
                nums[f],nums[m]=nums[m],nums[f]
                f+=1
                m+=1
            elif nums[m]==2:
                nums[l],nums[m]=nums[m],nums[l]
                l-=1
            else:
                m+=1
