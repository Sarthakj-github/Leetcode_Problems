class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        S = [0] * n        # prefix sums of digits
        P = [0] * n        # map index in s -> length of non-zero digits processed
        prefixInt = [0]    # prefix integer values of non-zero digits
        mod = 10**9 + 7

        for j in range(n):
            digit = int(s[j])
            S[j] = digit if j == 0 else S[j-1] + digit
            if digit != 0:
                prefixInt.append((prefixInt[-1] * 10 + digit) % mod)
            P[j] = len(prefixInt) - 1   # position in prefixInt after s[j]

        ans = []
        for i, j in queries:
            left = P[i-1] if i > 0 else 0
            right = P[j]

            if right > left:
                # extract integer slice using modular subtraction
                length = right - left
                val = (prefixInt[right] - (prefixInt[left] * pow(10, length, mod)) % mod + mod) % mod
                sum_val = S[j] - (S[i-1] if i > 0 else 0)
                ans.append((val * sum_val) % mod)
            else:
                ans.append(0)

        return ans
