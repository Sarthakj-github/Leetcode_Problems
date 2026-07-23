class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        
        n=len(nums)
        if n<3:
            return n

        ans=0
        while n:
            ans+=1
            n>>=1
        
        return 2**(ans)
