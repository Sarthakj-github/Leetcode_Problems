class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        n=len(nums)

        for i in range(n):
            s=0
            a=nums[i]
            while a:
                s+=a%10
                a//=10
            if s==i:
                return i
        
        return -1
