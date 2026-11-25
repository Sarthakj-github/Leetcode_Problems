class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        
        def has_unique(length: int) -> bool:
            base = 131
            mod = 10**9 + 9
            
            power = pow(base, length - 1, mod)
            counts = {}
            h = 0
            
            for i in range(length):
                h = (h * base + nums[i]) % mod
            counts[h] = counts.get(h, 0) + 1
            
            for i in range(length, n):
                h = (h - nums[i - length] * power) % mod
                h = (h * base + nums[i]) % mod
                counts[h] = counts.get(h, 0) + 1
                
            return any(c == 1 for c in counts.values())

        low, high = 1, n
        ans = n
        
        while low <= high:
            mid = (low + high) // 2
            if has_unique(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
