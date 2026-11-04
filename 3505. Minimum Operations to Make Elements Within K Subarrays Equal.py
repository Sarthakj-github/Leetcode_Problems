class Window:
    def __init__(self, values):
        self.h = len(values) // 2
        self.odd = len(values) & 1
        self.sorted = SortedList(values)
        self.low = sum(self.sorted[:self.h])
        self.total = sum(values)

    def get_cost(self):
        return self.total - 2 * self.low - self.odd * self.sorted[self.h]

    def slide(self, out, new):
        s = self.sorted
        h = self.h
        if new < s[h - 1]:
            self.low += new - s[h - 1]
        s.add(new)
        if out <= s[h - 1]:
            self.low += s[h] - out
        s.remove(out)
        self.total += new - out
        return self.get_cost()


class Solution:
    def minOperations(self, nums, x, k):
        win = Window(nums[:x])
        cost = [win.get_cost()] + [win.slide(o, n) for o, n in zip(nums, nums[x:])]
        best = [0] * (len(nums) + 1)
        for _ in range(k):
            best = list(accumulate([inf] * x + [b + c for b, c in zip(best, cost)], min))
        return best[-1]
