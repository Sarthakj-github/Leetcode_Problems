class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        b = sorted([(digit_sum(x), x, i) for i, x in enumerate(nums)])

        p = [0] * len(nums)
        for pos, (_, _, idx) in enumerate(b):
            p[pos] = idx

        vis = [False] * len(nums)
        ans = 0

        for i in range(len(nums)):
            if vis[i] or p[i] == i:
                continue

            cnt = 0
            j = i
            while not vis[j]:
                vis[j] = True
                j = p[j]
                cnt += 1

            ans += cnt - 1
        return ans
