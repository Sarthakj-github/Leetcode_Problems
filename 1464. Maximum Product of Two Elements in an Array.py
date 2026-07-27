class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums[0]>nums[1]:
            nums[0],nums[1]=nums[1],nums[0]
        for i in range(2,len(nums)):
            if nums[i]>nums[1]:
                nums[1],nums[0]=nums[i],nums[1]
            elif nums[i]>nums[0]:
                nums[0]=nums[i]
        return (nums[1]-1)*(nums[0]-1)
