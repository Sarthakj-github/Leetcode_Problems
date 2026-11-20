class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        d = {}
        
        for a in nums:
            d[a + 1] = d.get(a, 0) + 1
            d[a] = d.get(a - 1, 0) + 1
            
        return max(d.values())
