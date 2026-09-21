class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        if k == 1:
            return [n * (n + 1) // 2]

        nums = [num % k for num in nums]

        if k == 2:
            grps = groupby(nums)
            cnts = [len(list(grp)) for key, grp in grps if key != 0]
            odds = sum(c * (c + 1) // 2 for c in cnts)
            total = n * (n + 1) // 2
            return [total - odds, odds]

        res = [0] * k
        prev = [0] * k

        for num in nums:
            new = [0] * k
            rem = num % k
            new[rem] += 1

            for r in range(k):
                if prev[r]:
                    new[(r * num) % k] += prev[r]

            for r in range(k):
                res[r] += new[r]

            prev = new

        return res
