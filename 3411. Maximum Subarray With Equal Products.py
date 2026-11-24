import math

class Solution:
    def maxLength(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        # Upper bound to prune the inner loop when product grows too large
        max_p = math.lcm(*nums) * max(nums)
        
        for i in range(n):
            p = 1
            g = 0
            l = 1
            for j in range(i, n):
                p *= nums[j]
                g = math.gcd(g, nums[j])
                l = math.lcm(l, nums[j])
                
                if p == g * l:
                    ans = max(ans, j - i + 1)
                
                if p > max_p:
                    break
                    
        return ans
