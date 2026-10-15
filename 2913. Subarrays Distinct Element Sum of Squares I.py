class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n,s=len(nums),0
        for i in range(1,n+1):
            k,j=0,i
            while j<=n:
                s+=len(set(nums[k:j]))**2
                j+=1
                k+=1
        return s
