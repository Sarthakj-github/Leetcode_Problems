class Solution:
    def check(self, nums: List[int]) -> bool:
        n,i,p=len(nums),1,101
        while i<n:
            if not(nums[i-1]<=nums[i]<=p):
                if p==101 and nums[i]<=nums[0]:
                    p=nums[0]
                else:
                    return False
            i+=1
        return True
