class Solution:
    def minElement(self, nums: List[int]) -> int:
        m=40
        for num in nums:
            s=0
            while num:
                s+=(num%10)
                num//=10
            m=min(m,s)
        return m
