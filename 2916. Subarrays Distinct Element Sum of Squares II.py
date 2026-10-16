class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        size = 4 * n
        sumv = [0] * size
        sqv = [0] * size
        lazy = [0] * size

        def apply(idx, l, r, val):
            length = r - l + 1
            sqv[idx] += 2 * val * sumv[idx] + length * val * val
            sumv[idx] += length * val
            lazy[idx] += val

        def push(idx, l, r):
            if lazy[idx]:
                m = (l + r) // 2
                apply(idx * 2, l, m, lazy[idx])
                apply(idx * 2 + 1, m + 1, r, lazy[idx])
                lazy[idx] = 0

        def update(idx, l, r, ql, qr, val):
            if ql > r or qr < l:
                return
            if ql <= l and r <= qr:
                apply(idx, l, r, val)
                return
            push(idx, l, r)
            m = (l + r) // 2
            update(idx * 2, l, m, ql, qr, val)
            update(idx * 2 + 1, m + 1, r, ql, qr, val)
            sumv[idx] = sumv[idx * 2] + sumv[idx * 2 + 1]
            sqv[idx] = sqv[idx * 2] + sqv[idx * 2 + 1]

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, n - 1, p + 1, i, 1)
            ans = (ans + sqv[1]) % MOD
            last[x] = i
        return ans
