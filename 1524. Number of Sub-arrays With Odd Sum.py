class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        ans = 0
        odd_count = 0
        even_count = 1
        s = 0
        
        for x in arr:
            s ^= (x % 2)
            if s == 1:
                ans = (ans + even_count) % MOD
                odd_count += 1
            else:
                ans = (ans + odd_count) % MOD
                even_count += 1
                
        return ans
