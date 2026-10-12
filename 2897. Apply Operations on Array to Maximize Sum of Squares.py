class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7

        cnt = [0] * 30

        for num in nums:
            for bit in range(30):
                if (num >> bit) & 1:
                    cnt[bit] += 1

        total = 0

        for i in range(k):
            current = 0

            for bit in range(30):
                if cnt[bit] > i:
                    current |= (1 << bit)

            total += current * current

        return total % MOD
