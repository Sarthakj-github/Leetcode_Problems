class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        
        if sum(nums)==0:
            return 0
        n=len(nums)
        x=0
        for i in nums:
            x^=i
        
        if x==0:
            return n-1
        else:
            return n
