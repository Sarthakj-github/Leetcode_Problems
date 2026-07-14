class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)

        # dp[i][g1][g2]
        dp = [[[0] * 201 for _ in range(201)] for _ in range(n + 1)]
        dp[0][0][0] = 1

        for i in range(n):
            x = nums[i]

            for g1 in range(201):
                for g2 in range(201):
                    if dp[i][g1][g2] == 0:
                        continue

                    ways = dp[i][g1][g2]

                    # Ignore
                    dp[i + 1][g1][g2] = (dp[i + 1][g1][g2] + ways) % MOD

                    # Put in seq1
                    ng1 = x if g1 == 0 else gcd(g1, x)
                    dp[i + 1][ng1][g2] = (dp[i + 1][ng1][g2] + ways) % MOD

                    # Put in seq2
                    ng2 = x if g2 == 0 else gcd(g2, x)
                    dp[i + 1][g1][ng2] = (dp[i + 1][g1][ng2] + ways) % MOD

        ans = 0
        for g in range(1, 201):
            ans = (ans + dp[n][g][g]) % MOD

        return ans
