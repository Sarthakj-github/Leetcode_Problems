def divisors_n(n):
    d = []
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            d.append(i)
            if i * i != n:
                d.append(n // i)
    return sorted(d)

def cyclic_rotate_sort(a):
    k = len(a)

    cnt = 0
    pos = -1
    for i in range(k):
        if a[i] > a[(i + 1) % k]:
            cnt += 1
            pos = i
            if cnt > 1:
                return None

    if cnt == 0:
        return a

    return a[pos + 1:] + a[:pos + 1]

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for k in divisors_n(n):
            L = []

            for i in range(0, n, k):
                P = cyclic_rotate_sort(nums[i:i + k])

                if P is None:
                    L = []
                    break

                L.extend(P)

            if L and all(L[i] <= L[i + 1] for i in range(n - 1)):
                ans += k

        return ans
