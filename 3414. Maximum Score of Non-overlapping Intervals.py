class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        indexed = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        indexed.sort(key=lambda x: x[1])  # sort by end
        n = len(indexed)
        ends = [iv[1] for iv in indexed]

        def findPrev(i):
            return bisect.bisect_left(ends, indexed[i][0]) - 1

        # dp[i][k] = (weight, indices)
        dp = [[(0, []) for _ in range(5)] for _ in range(n+1)]

        for i in range(1, n+1):
            l, r, w, idx = indexed[i-1]
            j = findPrev(i-1)
            for k in range(1, 5):
                # skip
                skip = dp[i-1][k]
                # take
                take_w, take_idx = dp[j+1][k-1]
                take = (take_w+w, take_idx+[idx])
                # choose better
                if take[0] > skip[0] or (take[0]==skip[0] and sorted(take[1]) < sorted(skip[1])):
                    dp[i][k] = (take[0], sorted(take[1]))
                else:
                    dp[i][k] = skip

        return dp[n][4][1]
